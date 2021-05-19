import axios from 'axios';
import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from 'react-router-dom'

function Owner({match}) {
  const [owners, setOwner] = useState([])

  useEffect(() => {
    axios({
      method: "GET",
      url: `http://127.0.0.1:8000/api/owners`
  }).then(response =>{
      setOwner(response.data)
      })
  },[])

  return (
   <div>
            <table className='table'>
                <thead>
                <tr className="table-warning">
                    <td scope="col">Name</td>
                    <td scope="col">Address</td>
                    <td scope="col">Phone</td>
                    <td scope="col">Description</td>
                    <td scope="col">Image</td>

                </tr>
                </thead>
            <tbody>
                {owners.map(owner => (
                    <tr>
                        <td>{owner.name}</td>
                        <td>{owner.address}</td>
                        <td>{owner.phone}</td>
                        <td>{owner.description}</td>
                        <td><img src={owner.image} /></td>

                    </tr>
                ))}
            </tbody>
            </table>
        </div>

  );
}

export default Owner;