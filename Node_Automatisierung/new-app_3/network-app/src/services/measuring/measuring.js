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

}

export default new MeasuringData();