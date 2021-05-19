import axios from 'axios';
import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from 'react-router-dom'

function ExhibitionHall({match}) {
  const [exhibition_halls, setExhibition_halls] = useState([])

  useEffect(() => {
    axios({
      method: "GET",
      url: `http://127.0.0.1:8000/api/exhibition_halls`
  }).then(response =>{
      setExhibition_halls(response.data)
      })
  },[])

  return (
   <div>
            <table className='table'>
                <thead>
                <tr className="table-warning">
                    <td scope="col">Name</td>
                    <td scope="col">Owner</td>
                    <td scope="col">Square</td>
                    <td scope="col">Address</td>
                    <td scope="col">Phone</td>
                    <td scope="col">Description</td>
                    <td scope="col">Exhibitions</td>
                    <td scope="col">Image</td>

                </tr>
                </thead>
            <tbody>
                {exhibition_halls.map(exhibition_hall => (
                    <tr>
                        <td>{exhibition_hall.name}</td>
                        <td>{exhibition_hall.owner}</td>
                        <td>{exhibition_hall.square}</td>
                        <td>{exhibition_hall.address}</td>
                        <td>{exhibition_hall.phone}</td>
                        <td>{exhibition_hall.description}</td>
                        <td>{exhibition_hall.exhibitions}</td>
                        <td><img src={exhibition_hall.image} /></td>

                    </tr>
                ))}
            </tbody>
            </table>
        </div>

  );
}

export default ExhibitionHall;