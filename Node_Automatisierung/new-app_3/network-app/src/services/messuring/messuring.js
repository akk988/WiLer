import axios from 'axios';

// const API_URL = /api/ownAPI;
const API_URL = 'https://jsonplaceholder.typicode.com';


class MessuringData {
  
  async getAllData () {
    return await axios.get(API_URL + '/posts');
  }

}

export default new MessuringData();