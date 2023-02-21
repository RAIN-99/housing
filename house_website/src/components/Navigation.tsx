import React from 'react'
import {Link} from 'react-router-dom'

export function Navigation() {
  return (
    <nav className="h-[100px] flex justify-between px-5 bg-gray-500 items-center text-white">
      <span className="flex flex-row flex justify-between gap-px">
        <div className='w-20 mr-10'>
          <Link to="/houses/alatauskij" className="mr-2">Алатауский район</Link>
        </div>

        <div className='w-20 mx-10'>
          <Link to="/houses/almalinskij" className="mr-2">Алмалинский район</Link>
        </div>

        <div className='w-20 mx-10'>
          <Link to="/houses/aujezovskij" className="mr-2">Ауэзовский район</Link>
        </div>

        <div className='w-20 mx-10'>
          <Link to="/houses/bostandykskij" className="mr-2">Бостандыкский район</Link>
        </div>

        <div className='w-20 mx-10'>
          <Link to="/houses/medeuskij" className="mr-2">Медеуский район</Link>
        </div>

        <div className='w-20 mx-10'>
          <Link to="/houses/nauryzbajskiy" className="mr-2">Наурызбайский район</Link>
        </div>

        <div className='w-20 mx-10'>
          <Link to="/houses/turksibskij" className="mr-2">Турксибский район</Link>
        </div>

        <div className='w-20 ml-10'>
          <Link to="/houses/zhetysuskij" className="mr-2">Жетысуский район</Link>
        </div>
      </span>
      <span>
        <Link to="/login" className="mx-5">Sign in</Link>
        <Link to="/" className="mx-5">Main</Link>
        <Link to="/analytics" className="ml-5">Analytics</Link>
      </span>
    </nav>
  )
}