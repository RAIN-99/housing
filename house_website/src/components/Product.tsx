import React, {useState} from 'react'
import {IHouse} from '../models'

interface ProductProps {
  product: IHouse
}

export function Product({ product }: ProductProps) {
  const [details, setDetails] = useState(false)

  const btnBgClassName = details ? 'bg-yellow-400' : 'bg-blue-400'
  const btnClasses = ['py-2 px-4 border', btnBgClassName]

  return (
    <div
      className="border py-2 px-10 flex flex-col items-center mb-10 w-1/5"
    >
      <img src={product.image} className="w-1/1"/>
      <p className="font-bold">{product.price} тенге </p>
      <p>{ product.number_of_rooms }</p>
      { product.floor>0 &&  product.total_floor>0 && <p>{ product.floor }/{ product.total_floor } Этаж </p>}
      <p>{Math.round(product.area)} м²</p>
      <button
        className={btnClasses.join(' ')}
        onClick={() => setDetails(prev => !prev)}
      >
        { details ? 'Hide Details' : 'Show Details' }
      </button>

      {details && <div>
        <p>{product.description}</p>

      </div>}

    </div>
  )
}