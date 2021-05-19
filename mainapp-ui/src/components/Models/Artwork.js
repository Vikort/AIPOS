import axios from 'axios';
import React, {useState, useEffect} from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import {Link} from 'react-router-dom'

function Artwork({match}) {
  const [artworks, setArtworks] = useState([])

  useEffect(() => {
    axios({
      method: "GET",
      url: `http://127.0.0.1:8000/api/artworks`
  }).then(response =>{
      setArtworks(response.data)
      })
  },[])

  return (
   <div>
            <table className='table'>
                <thead>
                <tr className="table-warning">
                    <td scope="col">Name</td>
                    <td scope="col">Artist</td>
                    <td scope="col">Kind of work</td>
                    <td scope="col">Date</td>
                    <td scope="col">Height</td>
                    <td scope="col">Width</td>
                    <td scope="col">Volume</td>
                    <td scope="col">Description</td>
                    <td scope="col">Image</td>

                </tr>
                </thead>
            <tbody>
                {artworks.map(artwork => (
                    <tr>
                        <td>{artwork.name}</td>
                        <td>{artwork.artist}</td>
                        <td>{artwork.kind_of_work}</td>
                        <td>{artwork.date}</td>
                        <td>{artwork.height}</td>
                        <td>{artwork.width}</td>
                        <td>{artwork.volume}</td>
                        <td>{artwork.description}</td>
                        <td><img src={artwork.image} /></td>

                    </tr>
                ))}
            </tbody>
            </table>
        </div>

  );
}

export default Artwork;