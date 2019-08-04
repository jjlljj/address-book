const validateAddress = async e => {
  e.preventDefault();

  // organize refs & ref values
  const addressFormRef = document.querySelector('#address-form');
  const contactIdsList = [ 'first_name', 'last_name' ];
  const addressIdsList = [ 'address', 'city', 'state', 'zip_code' ]
  const contactData = formatIdsWithNodeAndValue(contactIdsList);
  const addressData = formatIdsWithNodeAndValue(addressIdsList);

  // clear error text
  renderError();

  // all name fields are not empty
  if (!contactIdsList.every(id => !!contactData[id].value)) {
    showInputError(contactIdsList, contactData) 
    return renderError('Please complete the first and last name fields');
  } else {
    hideInputError(contactIdsList, contactData) 
  }

  // all address fields are not empty
  if (!addressIdsList.every(id => !!addressData[id].value)) {
    showInputError(addressIdsList, addressData) 
    return renderError('Please complete the address fields.');
  } else  {
    hideInputError(addressIdsList, addressData) 
  }

  // need pull apiId into py env variable
  const apiId = '449SELF06473';

  // build usps api url
  const url = `https://secure.shippingapis.com/shippingapi.dll?API=ZipCodeLookup&XML=<ZipCodeLookupRequest USERID="${apiId}"><Address ID="0"><Address1></Address1><Address2>${addressData['address'].value}</Address2><City>${addressData['city'].value}</City><State>${addressData['state'].value}</State><Zip5>${addressData['zip_code'].value}</Zip5><Zip4></Zip4></Address></ZipCodeLookupRequest>`;

  // validate address with usps api
  const responseDoc = await doFetchUrlXml(url);

  // handle an invalid addrss
  if (responseDoc.getElementsByTagName('Error').length) {
    showInputError(addressIdsList, addressData) 
    return renderError('The entered address is not valid, please enter a valid address.');
  } else {
    // valid address
    const addressValues = parseAddressValuesFromXml(responseDoc);
    addressIdsList.forEach(id => addressData[id].ref.value = addressValues[id]);

    // submit form
    addressFormRef.submit();
  }
}

// fetch and parse xml
const doFetchUrlXml = async url => {
  try {
    const response = await fetch(url);
    const string = await response.text();
    const responseDoc = new DOMParser().parseFromString(string, 'application/xml');

    return responseDoc;
  } catch (err) {

    renderError('Something went wrong.');
  }
}

// format input node refs as obj with ref and current value
const formatIdsWithNodeAndValue = ids => {
  return ids.reduce((acc, id) => {
    let ref = document.querySelector(`#${id}`);
    let value = ref.value;
    return {...acc, [id]: { ref, value }};
  }, {});
}

// handle xml address values
const parseAddressValuesFromXml = responseDoc => {
  const address = responseDoc.getElementsByTagName('Address2')[0].textContent;
  const city = responseDoc.getElementsByTagName('City')[0].textContent;
  const state = responseDoc.getElementsByTagName('State')[0].textContent;
  const zip5 = responseDoc.getElementsByTagName('Zip5')[0].textContent;
  const zip4 = responseDoc.getElementsByTagName('Zip4')[0].textContent;
  const zip_code = `${zip5}-${zip4}`;

  return { address, city, state, zip_code };
}

const showInputError = (ids, data) => {
  ids.forEach(id => data[id].ref.classList.add('input-error'));
}

const hideInputError = (ids, data) => {
  ids.forEach(id => data[id].ref.classList.remove('input-error'));
}

const renderError = errorText => {
  const errorTextRef = document.querySelector('#error-text');
  errorTextRef.innerHTML = errorText || '';
}

