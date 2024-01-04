<script>
	import { ApolloClient, InMemoryCache } from '@apollo/client/core';
	import { setClient } from 'svelte-apollo';
	import Header from '../lib/components/Header.svelte';

	const cache = new InMemoryCache({
		typePolicies: {
			ColaboradorType: {
				keyFields: ['dniCifColaborador']
			}
		}
	});
	const client = new ApolloClient({
		uri: 'http://127.0.0.1:8000/graphql/',
		cache: cache
	});
	setClient(client);
</script>

<Header />

<slot />

<style>
	:global(a) {
		text-decoration: none;
		color: #0b1215;
	}
</style>
