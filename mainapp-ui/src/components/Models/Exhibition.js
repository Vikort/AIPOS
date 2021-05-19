import axios from 'axios';
import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from 'react-router-dom'

function Exhibition({match}) {
  const [exhibitions, setExhibition] = useState([])

  useEffect(() => {
    axios({
      method: "GET",
      url: `http://127.0.0.1:8000/api/exhibitions`
  }).then(response =>{
      setExhibition(response.data)
      })
  },[])

  return (
   <div>
            <table className='table'>
                <thead>
                <tr className="table-warning">
                    <td scope="col">Name</td>
                    <td scope="col">Kind</td>
                    <td scope="col">Date</td>
                    <td scope="col">Artworks</td>
                    <td scope="col">Description</td>
                    <td scope="col">Image</td>

                </tr>
                </thead>
            <tbody>
                {exhibitions.map(exhibition => (
                    <tr>
                        <td>{exhibition.name}</td>
                        <td>{exhibition.kind}</td>
                        <td>{exhibition.date}</td>
                        <td>{exhibition.artworks}</td>
                        <td>{exhibition.description}</td>
                        <td><img src={exhibition.image} /></td>

                    </tr>
                ))}
            </tbody>
            </table>
        </div>

  );
}

export default Exhibition;