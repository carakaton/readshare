<template>
    <h3 style="padding-top: 30px;">Найденные книги</h3>
    <div style="overflow:scroll; height:200px;">
        <post-item v-for="post in posts" :post="post" v-bind:key="post.id" @add="$emit('add', post)" />
    </div>
</template>

<script>
import PostItem from '@/components/PostItem';
export default {
    components: { PostItem },
    props: {
        posts: {
            type: Array,
            required: true
        }
    }
}
</script>

<style scoped>

</style>