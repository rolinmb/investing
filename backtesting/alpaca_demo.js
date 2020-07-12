const Alpaca = require('@alpacahq/alpaca-trade-api');
const keys = require('./config.js');

const api = new Alpaca({
	keyId: keys.AP_API_KEY,
	secretKey: keys.AP_API_SECRET,
	paper: true,
	usePolygon: false
});

api.getAccount().then((account) => {
	console.log('Alpaca API: ', account);
});

api.getOrders({status:'all'}).then((orders) => {
	console.log('\nOrder List: ', orders)
});

api.getPositions().then((positions) => {
	console.log('\nPositions List: ', positions)
});
api.getAccountActivities({activityTypes:'FILL'}).then((activities) => {
	console.log('\nAccount Activity List', activities);
});
/*
api.closeAllPositions().then((response) => {
	console.log(response)
});

api.cancelAllOrders().then((response) => {
	console.log(response)
});

*/
