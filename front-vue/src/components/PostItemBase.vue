<template>
    <div class ="postBase">
        <div >
            <div><strong>Название </strong>{{ postBase.title }}</div>
            <div><strong>Автор </strong>{{ postBase.author }}</div>
        </div>
        <div class="postBase__btns">
            <my-button @click="$emit('del', postBase)">Удалить из базы</my-button>
        </div>
    </div>
</template>

<script>
export default {
    props: {
        postBase:{
            type: Object,
            required: true,
        }
    }
}
</script>

<style scoped>
.postBase {
  padding: 15px;
  border: 2px solid teal;
  margin-top: 15px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}
</style>