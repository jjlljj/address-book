const deleteAddress = async e => {
e.preventDefault();
const { target } = e;

const address_id = target.getAttribute('data-id');

if (window.confirm("Delete This Address?")) { 
  try {
    const response = await fetch(`api/address_book/edit/${address_id}`, {
      method: 'DELETE',
      headers: {'Content-Type': 'application/json'},
    });

    const result = await response.json();

    if (result.success === true) {
      const addressElement = document.querySelector(`#address-${address_id}`);
      addressElement.remove();
    }
  } catch (err) {
    console.log(err);
  }
}
}
