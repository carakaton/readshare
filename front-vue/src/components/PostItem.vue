<template>
    <div class ="post">
        <div >
            <div><strong>Название </strong>{{ post.title }}</div>
            <div><strong>Автор </strong>{{ post.author }}</div>
        </div>
        <div class="post__btns">
            <my-button @click="$emit('add', post)">Добавить</my-button>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        post:{
            type: Object,
            required: true,
        }
    }
}
</script>

<style scoped>
.post {
  padding: 15px;
  border: 2px solid teal;
  margin-top: 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>