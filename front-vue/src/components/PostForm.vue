<template>
     <form @submit.prevent>
        <!-- <h4>добавление книги</h4>
        <input class="input" v-model="post.title" type="text" placeholder="Название">
        <input class="input" v-model="post.body" type="text" placeholder="Автор">
        
        <my-button @click="createPost" style="align-self: flex-end; margin-top: 15px;">Создать</my-button> -->
    </form>
</template>

<script>
export default {
    data() {
        return {
            post: {
                title: '',
                body: ''
            }
        }
    },
    methods: {
        createPost(){
            this.post.id = Date.now();
            this.$emit('create', this.post)
            this.post = {
                title: '',
                body: ''
            }
        }
    }

}
</script>

<style scoped>
form {
  display: flex;
  flex-direction: column;
}
.input {
  width: 100%;
  border:1px solid teal;
  padding: 10px 15px;
  margin-top: 15px;
}
</style>