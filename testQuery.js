// Load the AWS SDK for Node.js
var AWS = require('aws-sdk');
// Set the region
AWS.config.update({region: 'us-east-2'});

// Create DynamoDB service object
var ddb = new AWS.DynamoDB({apiVersion: '2012-08-10'});

var params = {
  ExpressionAttributeValues: {
    ':designer': {S: 'Maison Margiela'},
    ':category': {S: 'Shoes'},
    ':size' : {N: '12'},
    ':price' : {N: '150'}
  },
  ProjectionExpression: 'designer, category, size, price',
  FilterExpression: 'designer = :designer, category = :category, size = :size, price = :price',
  TableName: 'listings'
};

ddb.scan(params, function(err, data) {
  if (err) {
    console.log("Error", err);
  } else {
    //console.log("Success", data.Items);
    data.Items.forEach(function(element, index, array) {
      console.log(element.Title.S + " (" + element.Subtitle.S + ")");
    });
  }
});