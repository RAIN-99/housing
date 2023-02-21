import React, {useContext, useState} from 'react'
import { Modal } from '../components/Modal'
import {ModalContext} from '../context/ModalContext'
import { IHouse } from '../models'
import axios from 'axios'

export function Analytics() {
  const [data, setData] = useState({
    "number_of_rooms":"",
    "floor": "",
    "area":"",
    "total_floor":"",
    "region":"alatauskij"
  })
  
  const [prediction, setPrediction] = useState(null)

  function handle(e){
    const newData = {...data}
    console.log(e.target.id)
    console.log(e.target.value)
    newData[e.target.id] = e.target.id === "region" ?  e.target.value : Number(e.target.value)
    setData(newData)
    console.log(newData)
  }
  
  function submit(e){
    e.preventDefault()
    axios.post("http://127.0.0.1:8000/analytics/",data).
    then(res => {
      console.log(res.data)
      setPrediction(res.data['prediction'])
    })

  }

  return (
    <form className='flex flex-col flex-wrap mt-20' onSubmit={(e)=>{submit(e)}}>
      
      <select className="border py-2 px-4 mb-2 w-1/6 outline-0" id ={"region"} onChange={(e)=>handle(e)}>
        <option value="alatauskij">alatauskij</option>
        <option value="almalinskij">almalinskij</option>
        <option value="aujezovskij">aujezovskij</option>
        <option value="bostandykskij">bostandykskij</option>
        <option value="medeuskij">medeuskij</option>
        <option value="nauryzbajskiy">nauryzbajskiy</option>
        <option value="turksibskij">turksibskij</option>
        <option value="zhetysuskij">zhetysuskij</option>
      </select>

      <div className='flex flex-row items-center'>
        <input
          type="number"
          className="border py-2 px-4 mb-2 w-1/6 mr-2"
          placeholder="Количество комнат"
          id = "number_of_rooms"
          value = {data.number_of_rooms}
          onChange={(e)=>handle(e)}
        />
        <p className='mb-2'> - Количество комнат</p>
      </div>
      
      <div className='flex flex-row items-center'>
        <input
          type="number"
          className="border py-2 px-4 mb-2 w-1/6 mr-2"
          placeholder="Этаж"
          id = "floor"
          value = {data.floor}
          onChange={(e)=>handle(e)}
        />
        <p className='mb-2'> - Этаж</p>
      </div>

      <div className='flex flex-row items-center'>
        <input
          type="number"
          className="border py-2 px-4 mb-2 w-1/6 mr-2"
          placeholder="Площадь"
          id = "area"
          value = {data.area}
          onChange={(e)=>handle(e)}
        />
        <p className='mb-2'> - Площадь</p>
      </div>

      <div className='flex flex-row items-center'>
        <input
          type="number"
          className="border py-2 px-4 mb-2 w-1/6 mr-2"
          placeholder="Всего этажей"
          id = "total_floor"
          value = {data.total_floor}
          onChange={(e)=>handle(e)}
        />
        <p className='mb-2'> - Всего этажей</p>
      </div>

      {prediction && <div className='flex flex-row items-center'>
        <p> Моделированая цена   =</p>
        <p className='ml-1'>{prediction} тенге</p>
      </div>}
      <button type="submit" className="py-2 px-4 mt-10 ml-20 w-20 border bg-yellow-400">Create</button>
    </form>
    )
}