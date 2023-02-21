import React, {useContext} from 'react'
import {useGetHouses} from '../hooks/houses'
import {ModalContext} from '../context/ModalContext'
import {IHouse} from '../models'
import {Loader} from '../components/Loader'
import {ErrorMessage} from '../components/ErrorMessage'
import {Product} from '../components/Product'
import {Modal} from '../components/Modal'
import { useParams } from 'react-router-dom'

export function HousesPage() {
  const data = useParams()

  const {loading, error, products} = useGetHouses({
    area:String(data.area)
  })



  return (
    <div>
      <div style={{display: 'flex',justifyContent: 'center'}}>
        { loading && <Loader /> }
        { error && <ErrorMessage error={error} /> }
      </div>
      <div className="flex flex-row flex-wrap">
        { products.map(product => <Product product={product} key={product.id} />) }
      </div>
    </div>
  )
}