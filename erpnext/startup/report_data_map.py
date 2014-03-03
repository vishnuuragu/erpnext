# Copyright (c) 2013, Web Notes Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt

from __future__ import unicode_literals

# mappings for table dumps
# "remember to add indexes!"

data_map = {
	"Company": {
		"columns": ["name"],
		"conditions": ["docstatus < 2"]
	},
	"Fiscal Year": {
		"columns": ["name", "year_start_date", "year_end_date"],
		"conditions": ["docstatus < 2"],
	},

	# Accounts
	"Account": {
		"columns": ["name", "parent_account", "lft", "rgt", "root_type", 
			"is_pl_account", "company", "group_or_ledger"],
		"conditions": ["docstatus < 2"],
		"order_by": "lft",
		"links": {
			"company": ["Company", "name"],
		}
		
	},
	"Cost Center": {
		"columns": ["name", "lft", "rgt"],
		"conditions": ["docstatus < 2"],
		"order_by": "lft"
	},
	"GL Entry": {
		"columns": ["name", "account", "posting_date", "cost_center", "debit", "credit", 
			"is_opening", "company", "voucher_type", "voucher_no", "remarks"],
		"order_by": "posting_date, account",
		"links": {
			"account": ["Account", "name"],
			"company": ["Company", "name"],
			"cost_center": ["Cost Center", "name"]
		}
	},

	# Stock
	"Item": {
		"columns": ["name", "if(item_name=name, '', item_name) as item_name", "description", 
			"item_group as parent_item_group", "stock_uom", "brand", "valuation_method", 
			"re_order_level", "re_order_qty"],
		# "conditions": ["docstatus < 2"],
		"order_by": "name",
		"links": {
			"parent_item_group": ["Item Group", "name"],
			"brand": ["Brand", "name"]
		}
	},
	"Item Group": {
		"columns": ["name", "parent_item_group"],
		# "conditions": ["docstatus < 2"],
		"order_by": "lft"
	},
	"Brand": {
		"columns": ["name"],
		"conditions": ["docstatus < 2"],
		"order_by": "name"
	},
	"Project": {
		"columns": ["name"],
		"conditions": ["docstatus < 2"],
		"order_by": "name"
	},
	"Warehouse": {
		"columns": ["name"],
		"conditions": ["docstatus < 2"],
		"order_by": "name"
	},
	"Stock Ledger Entry": {
		"columns": ["name", "posting_date", "posting_time", "item_code", "warehouse", 
			"actual_qty as qty", "voucher_type", "voucher_no", "project",
			"ifnull(incoming_rate,0) as incoming_rate", "stock_uom", "serial_no"],
		"order_by": "posting_date, posting_time, name",
		"links": {
			"item_code": ["Item", "name"],
			"warehouse": ["Warehouse", "name"],
			"project": ["Project", "name"]
		},
		"force_index": "posting_sort_index"
	},
	"Serial No": {
		"columns": ["name", "purchase_rate as incoming_rate"],
		"conditions": ["docstatus < 2"],
		"order_by": "name"
	},
	"Stock Entry": {
		"columns": ["name", "purpose"],
		"conditions": ["docstatus=1"],
		"order_by": "posting_date, posting_time, name",
	},
	"Production Order": {
		"columns": ["name", "production_item as item_code", 
			"(ifnull(qty, 0) - ifnull(produced_qty, 0)) as qty", 
			"fg_warehouse as warehouse"],
		"conditions": ["docstatus=1", "status != 'Stopped'", "ifnull(fg_warehouse, '')!=''",
			"ifnull(qty, 0) > ifnull(produced_qty, 0)"],
		"links": {
			"item_code": ["Item", "name"],
			"warehouse": ["Warehouse", "name"]
		},
	},
	"Material Request Item": {
		"columns": ["item.name as name", "item_code", "warehouse", 
			"(ifnull(qty, 0) - ifnull(ordered_qty, 0)) as qty"],
		"from": "`tabMaterial Request Item` item, `tabMaterial Request` main",
		"conditions": ["item.parent = main.name", "main.docstatus=1", "main.status != 'Stopped'",
			"ifnull(warehouse, '')!=''", "ifnull(qty, 0) > ifnull(ordered_qty, 0)"],
		"links": {
			"item_code": ["Item", "name"],
			"warehouse": ["Warehouse", "name"]
		},
	},
	"Purchase Order Item": {
		"columns": ["item.name as name", "item_code", "warehouse", 
			"(ifnull(qty, 0) - ifnull(received_qty, 0)) as qty"],
		"from": "`tabPurchase Order Item` item, `tabPurchase Order` main",
		"conditions": ["item.parent = main.name", "main.docstatus=1", "main.status != 'Stopped'", 
			"ifnull(warehouse, '')!=''", "ifnull(qty, 0) > ifnull(received_qty, 0)"],
		"links": {
			"item_code": ["Item", "name"],
			"warehouse": ["Warehouse", "name"]
		},
	},
	
	"Sales Order Item": {
		"columns": ["item.name as name", "item_code", "(ifnull(qty, 0) - ifnull(delivered_qty, 0)) as qty", "warehouse"],
		"from": "`tabSales Order Item` item, `tabSales Order` main",
		"conditions": ["item.parent = main.name", "main.docstatus=1", "main.status != 'Stopped'", 
			"ifnull(warehouse, '')!=''", "ifnull(qty, 0) > ifnull(delivered_qty, 0)"],
		"links": {
			"item_code": ["Item", "name"],
			"warehouse": ["Warehouse", "name"]
		},
	},

	# Sales
	"Customer": {
		"columns": ["name", "if(customer_name=name, '', customer_name) as customer_name", 
			"customer_group as parent_customer_group", "territory as parent_territory"],
		"conditions": ["docstatus < 2"],
		"order_by": "name",
		"links": {
			"parent_customer_group": ["Customer Group", "name"],
			"parent_territory": ["Territory", "name"],
		}
	},
	"Customer Group": {
		"columns": ["name", "parent_customer_group"],
		"conditions": ["docstatus < 2"],
		"order_by": "lft"
	},
	"Territory": {
		"columns": ["name", "parent_territory"],
		"conditions": ["docstatus < 2"],
		"order_by": "lft"
	},
	"Sales Invoice": {
		"columns": ["name", "customer", "posting_date", "company"],
		"conditions": ["docstatus=1"],
		"order_by": "posting_date",
		"links": {
			"customer": ["Customer", "name"],
			"company":["Company", "name"]
		}
	},
	"Sales Invoice Item": {
		"columns": ["name", "parent", "item_code", "qty", "base_amount"],
		"conditions": ["docstatus=1", "ifnull(parent, '')!=''"],
		"order_by": "parent",
		"links": {
			"parent": ["Sales Invoice", "name"],
			"item_code": ["Item", "name"]
		}
	},
	"Sales Order": {
		"columns": ["name", "customer", "transaction_date as posting_date", "company"],
		"conditions": ["docstatus=1"],
		"order_by": "transaction_date",
		"links": {
			"customer": ["Customer", "name"],
			"company":["Company", "name"]
		}
	},
	"Sales Order Item[Sales Analytics]": {
		"columns": ["name", "parent", "item_code", "qty", "base_amount"],
		"conditions": ["docstatus=1", "ifnull(parent, '')!=''"],
		"order_by": "parent",
		"links": {
			"parent": ["Sales Order", "name"],
			"item_code": ["Item", "name"]
		}
	},
	"Delivery Note": {
		"columns": ["name", "customer", "posting_date", "company"],
		"conditions": ["docstatus=1"],
		"order_by": "posting_date",
		"links": {
			"customer": ["Customer", "name"],
			"company":["Company", "name"]
		}
	},
	"Delivery Note Item[Sales Analytics]": {
		"columns": ["name", "parent", "item_code", "qty", "base_amount"],
		"conditions": ["docstatus=1", "ifnull(parent, '')!=''"],
		"order_by": "parent",
		"links": {
			"parent": ["Delivery Note", "name"],
			"item_code": ["Item", "name"]
		}
	},
	"Supplier": {
		"columns": ["name", "if(supplier_name=name, '', supplier_name) as supplier_name", 
			"supplier_type as parent_supplier_type"],
		"conditions": ["docstatus < 2"],
		"order_by": "name",
		"links": {
			"parent_supplier_type": ["Supplier Type", "name"],
		}
	},
	"Supplier Type": {
		"columns": ["name"],
		"conditions": ["docstatus < 2"],
		"order_by": "name"
	},
	"Purchase Invoice": {
		"columns": ["name", "supplier", "posting_date", "company"],
		"conditions": ["docstatus=1"],
		"order_by": "posting_date",
		"links": {
			"supplier": ["Supplier", "name"],
			"company":["Company", "name"]
		}
	},
	"Purchase Invoice Item": {
		"columns": ["name", "parent", "item_code", "qty", "base_amount"],
		"conditions": ["docstatus=1", "ifnull(parent, '')!=''"],
		"order_by": "parent",
		"links": {
			"parent": ["Purchase Invoice", "name"],
			"item_code": ["Item", "name"]
		}
	},
	"Purchase Order": {
		"columns": ["name", "supplier", "transaction_date as posting_date", "company"],
		"conditions": ["docstatus=1"],
		"order_by": "posting_date",
		"links": {
			"supplier": ["Supplier", "name"],
			"company":["Company", "name"]
		}
	},
	"Purchase Order Item[Purchase Analytics]": {
		"columns": ["name", "parent", "item_code", "qty", "base_amount"],
		"conditions": ["docstatus=1", "ifnull(parent, '')!=''"],
		"order_by": "parent",
		"links": {
			"parent": ["Purchase Order", "name"],
			"item_code": ["Item", "name"]
		}
	},
	"Purchase Receipt": {
		"columns": ["name", "supplier", "posting_date", "company"],
		"conditions": ["docstatus=1"],
		"order_by": "posting_date",
		"links": {
			"supplier": ["Supplier", "name"],
			"company":["Company", "name"]
		}
	},
	"Purchase Receipt Item[Purchase Analytics]": {
		"columns": ["name", "parent", "item_code", "qty", "base_amount"],
		"conditions": ["docstatus=1", "ifnull(parent, '')!=''"],
		"order_by": "parent",
		"links": {
			"parent": ["Purchase Receipt", "name"],
			"item_code": ["Item", "name"]
		}
	},
	# Support
	"Support Ticket": {
		"columns": ["name","status","creation","resolution_date","first_responded_on"],
		"conditions": ["docstatus < 2"],
		"order_by": "creation"
	}
	
}
