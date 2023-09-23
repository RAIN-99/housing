import {useEffect, useState} from 'react'
import {IHouse} from '../models'
import axios, {AxiosError,AxiosRequestConfig } from 'axios'

interface IData {
  area: String,
}
export const useGetHouses = (params: IData) => {
  const [products, setProducts] = useState<IHouse[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState('')
  const area = params.area

  async function fetchProducts() {
    try {
      setError('')
      setLoading(true)
      const response = await axios.get<IHouse[]>(`http://localhost:8000/${area}/`)
      setProducts(response.data)
      setLoading(false)
    } catch (e: unknown) {
      const error = e as AxiosError
      setLoading(false)
      setError(error.message)
    }
  }

  useEffect(() => {
    if(!area){
      return
    }
    fetchProducts()
  },[area])

  return { products, error, loading }
}