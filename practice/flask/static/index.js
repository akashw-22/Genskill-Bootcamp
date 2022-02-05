function onLoad(response)
{
	console.log("aa ivde ethind");
	var content = $("<span>", {html : "The value of pi using " + response.algorithm + " is " + response.estimate + ". Bonus text : " + response.text});
	console.log(response);
	$("#estimate").html(content);
}


function onSubmit(event)
{
	event.preventDefault();	//prevents the default event from happening
	console.log("ellarum oombi\n"); //printing to the console
	var data = $(event.target).serialize();	//encodes the html ig :)
	var url = (event.target)['action'];	// target url of the event :|
	console.log(data);
	console.log(url);
	$("#estimate").html("Loading...");	//loading screen most probably ;(
	$.post({url : url,	//send request to the server using a https post request
			headers : {"Accept" : "applications/json"},	//explicitly telling the backend to send in json format
			data : data,
			success : onLoad});
	
}

function main()
{
	console.log("Hello myran\noombikko nee\n");
	$("form").submit(onSubmit);
}

$(main);
