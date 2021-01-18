import axios from 'axios';

// const API_URL = /api/ownAPI;
const API_URL = 'https://jsonplaceholder.typicode.com';

const REST_API = 'http://localhost:3000';


class MeasuringData {
  
  async getAllData () {
    return await axios.get(API_URL + '/posts');
  }

  async ownRestApi () {
    return await axios.get(REST_API + '/posts');
  }

  async getFromDB () {
    return await axios.get(REST_API + '/measuringdata')
        .then(
          message => {
            console.log("(axios)Data from Database: ", message.data);
            return message.data;
          })
        .catch(err => {
          console.log("(axios)ERROR from Database: ", err.message);
          return err.message;
        });
  }

  async postIntoDB (inputData) {
      console.log();
    return await axios.post(REST_API + '/postmeasuringdata',inputData)
        .then(
            message => {
              console.log("(axios)Data into Database: ", message.data);
              return message.data;
            })
        .catch(err => {
          console.log("(axios)ERROR from Database: ", err.message);
          return err.message;
        });
  }

}

export default new MeasuringData();