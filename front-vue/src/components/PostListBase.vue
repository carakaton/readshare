<template>
    <div>
        <h3 style="padding-top: 30px;">Коллекция</h3>
        <post-item-base v-for="postBase in postsBase" :postBase="postBase" v-bind:key="postBase.id" @del="$emit('del', postBase)"/>
    </div>
</template>

<script>
import PostItemBase from '@/components/PostItemBase';
export default {
    components: { PostItemBase },
    props: {
        postsBase: {
            type: Array,
            required: true
        }
    }
}
</script>

<style scoped>

</style>