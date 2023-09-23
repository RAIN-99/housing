import requests
from bs4 import BeautifulSoup
import csv
import time
import shutil
from PIL import Image
import pandas as pd
import re
from category_encoders import CountEncoder
import dill
import pandas as pd
from sklearn.model_selection import KFold, GridSearchCV, cross_validate,train_test_split
from sklearn.pipeline import Pipeline
from xgboost import XGBRegressor
import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from decouple import config
from sqlalchemy.types import *

config.encoding = 'cp1251'


pg_user = config("POSTGRES_USER")
pg_password = config("POSTGRES_PASSWORD")
pg_port = config("POSTGRES_PORT")
pg_db = config("POSTGRES_DB")
pg_host=config("POSTGRES_HOST")

AREAS_LIST = [
    "medeuskij",
    "alatauskij",
    "almalinskij",
    "aujezovskij",
    "bostandykskij",
    "zhetysuskij",
    "nauryzbajskiy",
    "turksibskij"
]


engine=create_engine(f"postgresql+psycopg2://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}")
# if not database_exists(engine.url):
#     create_database(engine.url)
# print(database_exists(engine.url))

df_schema = {
  "id": INTEGER,    
  "number_of_rooms": String(64),
  "price": INTEGER,
  "floor": INTEGER,
  "area": DECIMAL(15,4),
  "image": String(128),
  "total_floor": INTEGER,
  "description":String(512)
}

def get_page_data_and_save(html,name):
    soup = BeautifulSoup(html, 'lxml') 
    divs = soup.find('section', class_='a-list') 
    ads = divs.find_all('div', class_='a-card__inc')

    for ad in ads:
    
        try:
            div = ad.find('a', class_='a-card__title').text
            kv = div.split(",")[0] 
        except:
            kv = ''

        try:
            div = ad.find('a', class_='a-card__title').text
            square = div.split(",")[1]
        except:
            square  = ''

        try:
            div = ad.find('a', class_='a-card__title').text
            etaj = div.split(",")[2]
        except:
            etaj  = ''            

        try:
            price = ad.find('div', class_='a-card__price').text.strip()
        except:
            price = ''
        
        try:
            image_url = ad.find('img')['src']
            # img = Image.open(requests.get(image_url,stream=True).raw)
            # img.save(f"{kv}{price}{square}.png")
        except:
            image_url = ''
        
        try:
            descr = ad.find('div', class_='a-card__text-preview').text.strip()
        except:
            descr = ''
        
        data = {
            'title':kv,
            'price':price,
            'etaj':etaj,
            'square':square,
            "image":image_url,
            "description":descr
            }
        
        with open(f'./data.csv', 'a', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow((
                data['title'],
                data['price'],
                data['etaj'],
                data['square'],
                data["image"],
                data["description"]
            ))


def find_number(text):
    num = re.findall(r'\d+(?:\.\d+)?',text)
    return " ".join(num)


def featureAdding(data):
    # data["number_of_rooms"] = data["number_of_rooms"].apply(lambda x:find_number(x)).astype(int)
    
    data['price']=data['price'].apply(lambda x:find_number(x))
    data['price']=data['price'].str.replace(' ','').astype(float)

    data['floor']=(data['floor'].apply(lambda x: str(x).split('этаж')[0].strip())).str.replace(' ',"")
    data['total_floor']=data['floor'].apply(lambda x: str(x).split('/',1)[-1])
    data['floor']=data['floor'].apply(lambda x: str(x).split('/')[0])

    data['area']=data['area'].apply(lambda x:find_number(x))
    data['area']=data['area'].str.replace(' ','').astype(float)

    return data


def data_cleaning(data):
    data=data.drop_duplicates(subset=['number_of_rooms','area','floor','total_floor','price'])
    incorrect_prices_under = data[data['price']<1000000].index
    data = data.drop(index=incorrect_prices_under)
    incorrect_prices_over = data[data['price']>1000000000].index
    data = data.drop(index=incorrect_prices_over)
    incorrect_area_under = data[data['area']<10].index
    data = data.drop(index=incorrect_area_under)
    incorrect_area_over = data[data['area']>500].index
    data = data.drop(index=incorrect_area_over)
    data['floor']=data['floor'].astype(float)
    data['total_floor']=data['total_floor'].astype(float)
    incorrect_year_floor_under=data[data['floor']<1].index
    data = data.drop(index=incorrect_year_floor_under)
    incorrect_year_floor_over=data[data['floor']>30].index
    data = data.drop(index=incorrect_year_floor_over)
    incorrect_year_total_floor_under=data[data['total_floor']<1].index
    data = data.drop(index=incorrect_year_total_floor_under)
    incorrect_year_total_floor_over = data[data['total_floor']>30].index
    data = data.drop(index=incorrect_year_total_floor_over)
    
    return data


def fill_missing_values(data):

    categorical_columns = data.select_dtypes(object).columns.tolist()
    data[categorical_columns] = data[categorical_columns].fillna("MISSING")

    numerical_columns = data.select_dtypes('number').columns.tolist()
    data[numerical_columns] = data[numerical_columns].fillna(-999)

    incorrect_index=data[data['price']<0].index
    data=data.drop(index=incorrect_index)
    data.reset_index()

    return data

def modeling(data):
    full_data=data

    features, target = full_data.drop(columns=['price',"image", "description"]), full_data['price']
    X_train,X_test,y_train,y_test=train_test_split(features,target,shuffle=True)
    # pd.DataFrame(X_train).to_csv(f'./models/{i}/X_train.csv',index=False)
    # pd.DataFrame(X_test).to_csv(f'./models/{i}/X_test.csv',index=False)
    # pd.DataFrame(y_train).to_csv(f'./models/{i}/y_train.csv',index=False)
    # pd.DataFrame(y_test).to_csv(f'./models/{i}/y_test.csv',index=False)
    
    categorical_columns = X_train.select_dtypes(object).columns
    scoring=['r2', 'neg_root_mean_squared_error']
    print("Shape of Data", X_train.shape,y_train.shape)
    pipeline = Pipeline(steps=[('encoder', CountEncoder(cols=categorical_columns,
                                                        min_group_size=1,
                                                        handle_unknown=0)),
                            ('regressor', XGBRegressor(n_estimators=1000,
                                                        verbosity=0,
                                                        reg_lambda=0.4,
                                                        reg_alpha=0.4,
                                                        sample_type='uniform',
                                                        rate_drop=0.1,
                                                        base_score=0.5,
                                                        booster='gbtree',
                                                        subsample=1,
                                                        colsample_bylevel=1,
                                                        colsample_bynode=1,
                                                        colsample_bytree=1,
                                                        gamma=0.1,
                                                        importance_type='gain',
                                                        max_delta_step=0,
                                                        min_child_weight=1,
                                                        n_jobs=4,
                                                        objective='reg:squarederror',
                                                        max_depth=4,
                                                        learning_rate=0.07,
                                                        random_state=5)
    )])


    params = {
        'regressor__n_estimators' : [800],
        'regressor__max_depth' : [4],
        'regressor__learning_rate' : [0.07],
        'regressor__reg_lambda':[0.4],
        'regressor__reg_alpha':[0.4],
        'regressor__gamma':[0.1],
        'regressor__rate_drop':[0,0.3],
        'regressor__subsample':[1]
    }

    kfold_generator = KFold(n_splits=10, shuffle=True, random_state=5)
    
    search = GridSearchCV(pipeline, params, cv=kfold_generator, scoring=scoring, n_jobs=4, verbose=0, refit='neg_root_mean_squared_error')
    search.fit(X_train,y_train)
    best_model = search.best_estimator_
    # X_test['prediction']=best_model.predict(X_test)
    # X_test['true_value']=y_test
    # X_test.to_csv(f'./models/{i}/comparison_results.csv',index=False)
    return best_model



def clean():
    data = pd.read_csv(f'./data.csv',header=None,names=['number_of_rooms','price','floor','area', "image", "description"])
    data = featureAdding(data)
    data = data_cleaning(data)
    data = fill_missing_values(data)
    return data


def main():
    for name in AREAS_LIST:
        print("Parsing",name)
        base_url_with_page = f"https://krisha.kz/prodazha/kvartiry/almaty-{name}/?page="
        # os.remove(f'./models/Xgboost_model_{name}.pkl')
        for i in range(1, 10):
            try:
                url_gen = base_url_with_page + str(i)
                html = requests.get(url_gen).text
                get_page_data_and_save(html,name)
                time.sleep(5)
            except:
                print("Error")


        print("Clean and Save", name)
        full_data = clean()
        os.remove(f'./data.csv')

        # print("Modeling",name)
        # model = modeling(full_data)

        # print("Save Model",name)
        # dill.dump(model, open(f'./models/Xgboost_model_{name}.pkl', 'wb'))
        
        try:
            full_data.to_sql(f'houses_{name}', engine, if_exists= 'replace', index=True, index_label="id", dtype=df_schema)
        
        except:
            print("Data not saved in database")


if __name__ == "__main__":
    main()