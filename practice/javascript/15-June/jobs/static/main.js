function handleupdate(res)
{
	console.log(res);
	$("#desc").html(res);
}

function handleclick(sambhavam)
{
	console.log("click seythu");
	$("#desc").html("Loading...");
	var link = sambhavam.target['href'];	//target is the html code for the event(sambhavam)
											//the href returns the href-link fot it
	$.get(link).done(handleupdate);			//jquery sending requests and when reqeust is done
											//goto handle update
	sambhavam.preventDefault();
}

function main(){
	var links = ($("a.joblink")); //this is a javascript variable named links (selected similar
								//to css
	links.click(handleclick);	//as the links are clicked, the function handleclick is called
}

$(main); //this is jquery it loads after the page is loaded
