//To Start server go in terminal and go to bash type "node *name of file*"
//Control C to end server

//Importing two libraries - http & fs
const http = require('http') //Used to start the server
const fs = require('fs') //Does all file handleing
const port = 3000 //Tells code what port to listen to for server

const server = http.createServer(function(req,res) {            //Creates server with request and response parameters, inside of function someones requests page it will call this function
    res.writeHead(200, { 'Content-Type': 'text/html'})  //rendering html for server
    fs.readFile('index.html', function(error, data) { //function takes name of file and takes function with error property if there is error and data argument all data inside file
        if (error) {    //check if error, tell browsers can't find it
            res.writeHead(404) 
            res.write('Error: File Not Found')
        }   else {
            res.write(data) //writes data from file if no error
        } 
        res.end()
    } )
})

//Setting up server so it listens to port we set it to 
server.listen(port, function(error) {
    //So we can check logs to see if anything wrong or working
    if (error){
        console.log('Something went wrong', error)
    }   else{ 
        console.log('Server is listening on port' + port)
    }
})