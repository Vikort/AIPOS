import axios from 'axios';
import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from 'react-router-dom'

function Artist({match}) {
  const [artists, setArtist] = useState([])

  useEffect(() => {
    axios({
      method: "GET",
      url: `http://127.0.0.1:8000/api/artists`
  }).then(response =>{
      setArtist(response.data)
      })
  },[])

  return (
   <div>
            <table className='table'>
                <thead>
                <tr className="table-warning">
                    <td scope="col">Name</td>
                    <td scope="col">Place of birth</td>
                    <td scope="col">Date of birth</td>
                    <td scope="col">Biography</td>
                    <td scope="col">Education</td>
                    <td scope="col">Image</td>

                </tr>
                </thead>
            <tbody>
                {artists.map(artist => (
                    <tr>
                        <td>{artist.name}</td>
                        <td>{artist.place_of_birth}</td>
                        <td>{artist.date_of_birth}</td>
                        <td>{artist.biography}</td>
                        <td>{artist.education}</td>
                        <td><img src={artist.image} /></td>

                    </tr>
                ))}
            </tbody>
            </table>
        </div>

  );
}

export default Artist;