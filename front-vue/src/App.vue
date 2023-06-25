<template>
  <div class="app">
    <h3>Поиск книг</h3>
    <input class="input" id="input_value" type="text" placeholder="Название и / или автор книги">
    <my-button @click="fetchPosts" style="margin-top: 15px;">Найти</my-button>
    <post-form @create="createPost"/>
    <post-list :posts="posts" @add="addPost"/>
    <post-list-base :postsBase="postsBase" @del="delPost"/>
    <my-button @click="getAllPost" style="margin-top: 15px;">Обновить</my-button>
  </div>
</template>

<script>
import PostForm from "@/components/PostForm";
import PostList from "@/components/PostList";
import PostListBase from "@/components/PostListBase";
import axios from 'axios';

export default {
  components: {
    PostList, PostListBase, PostForm
  },
  data() {
    return{
      posts: [
    ],
      postsBase: [
    ],
    }
  },
  methods: {
    createPost(post) {
      this.posts.push(post);
    },
    /*removePost(post){
      this.posts = this.posts.filter(p => p.id !== post.id)
    }, */
    async fetchPosts() {
      try {
        var x = document.getElementById('input_value').value;
        const response = await axios.get(`http://localhost:8000/book/find/${x}`);
        console.log(response.data.books);
        this.posts = response.data.books; 
      } catch (e) {
        alert('Ошибка')
      }
    },
    async addPost(post) {
      try {
        const response2 = await axios.post(`http://localhost:8000/book/?livelib_id=${post.livelib_id}`);
        console.log(response2);
      } catch (e) {
        alert('Ошибка')
      }
    }, 
    async delPost(postBase) {
      try {
        const response3 = await axios.delete(`http://localhost:8000/book/${postBase.id}`);
        console.log(response3);
      } catch (e) {
        alert('Ошибка')
      }
    }, 
    async getAllPost() {
      try {
        const response4 = await axios.get(`http://localhost:8000/book/all`);
        console.log(response4);
        this.postsBase = response4.data.books; 
      } catch (e) {
        alert('Ошибка')
      }
    }, 
  }
} 
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
.app {
  padding: 20px;
}
.input {
  width: 100%;
  border:1px solid teal;
  padding: 10px 15px;
  margin-top: 15px;
}
</style>