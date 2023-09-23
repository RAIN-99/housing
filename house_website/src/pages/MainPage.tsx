import React, {useContext} from 'react'
import {useGetHouses} from '../hooks/houses'
import {ModalContext} from '../context/ModalContext'
import {IHouse} from '../models'
import {Loader} from '../components/Loader'
import {ErrorMessage} from '../components/ErrorMessage'
import {Product} from '../components/Product'
import {Modal} from '../components/Modal'
import { useParams } from 'react-router-dom'

export function MainPage(){
    return(
        <div style={{display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center',
                    height: '100vh'}}>
            <p style={{fontSize:20, paddingLeft:50, paddingRight:50, paddingTop:15}}>
            </p>
        </div>
    )
}