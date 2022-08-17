/*let body = {
  user:1,
  content: "i am from Client Side",
  image: null
}
    fetch("http://127.0.0.1:8000/apiv1/status/create/",{
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(body),
    })
      .then(response=>response.json())
      .then(data=>console.log(data))


*/
//get request
//axios.get("http://127.0.0.1:8000/apiv1/status/list/")
//.then(response=>console.log(response))

//post request
// let status = {
//   user : 1,
//   content: "I am another client data!",
//   image: null
// }
// axios.post("http://127.0.0.1:8000/apiv1/status/create/", status ,{
//    headers: {
//      "Content-Type": "application/json"
//    }
// })
//   .then(response => console.log(response))

//details request
  // axios.get("http://127.0.0.1:8000/apiv1/status/details/1")
  // .then(response=>console.log(response))

//delete request

// axios.delete("http://127.0.0.1:8000/apiv1/status/delete/10")
// .then(response=>console.log(response))


// UPDATE request:
//PUT method-- have to sent whole entity:

//let updated_status = {
//    user : 1,
//    content: "I have been updated!",
//    image: null
// }
// axios.put("http://127.0.0.1:8000/apiv1/status/update/9/",updated_status,{
//   headers:{
//     "Content-Type": "application/json"
//   }
// })
//   .then(response=>console.log(response))



  // UPDATE request:
  //PATCH method--only the update portion:

let updated_status = {
  content: "I have been updated using patch!"
}
axios.patch("http://127.0.0.1:8000/apiv1/status/update/9/",updated_status,{
 headers:{
   "Content-Type": "application/json"
 }
})
 .then(response=>console.log(response))

//completed crud process api
