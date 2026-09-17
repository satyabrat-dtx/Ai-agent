# DB2ADMIN.PLANTINVOICETRANSACTION

- **Module**: `INVENTORY` (low confidence — FK neighbourhood: 1 of 1 related tables are INVENTORY)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `PLANTINVOICECOMPANYCODE`, `PLANTINVOICEDIVISIONCODE`, `PLANTINVOICECODE`, `STOCKTRNTRANSACTIONNUMBER`, `STOCKTRNTRNDETAILNUMBER`, `INVOICELINENO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 141757

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PLANTINVOICECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PLANTINVOICECODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `INVOICELINENO` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PLANTINVOICE_PLANTINVOICETRANSACTION` | `PLANTINVOICECOMPANYCODE`, `PLANTINVOICEDIVISIONCODE`, `PLANTINVOICECODE` | [`PLANTINVOICE`](../CORE_MASTER/PLANTINVOICE.md) | `COMPANYCODE`, `DIVISIONCODE`, `CODE` | RESTRICT | `PLANTINVOICETRANSACTION.PLANTINVOICECOMPANYCODE = PLANTINVOICE.COMPANYCODE AND PLANTINVOICETRANSACTION.PLANTINVOICEDIVISIONCODE = PLANTINVOICE.DIVISIONCODE AND PLANTINVOICETRANSACTION.PLANTINVOICECODE = PLANTINVOICE.CODE` |
| `STOCKTRANSACTION_STOCKTRANSACTION` | `PLANTINVOICECOMPANYCODE`, `STOCKTRNTRANSACTIONNUMBER`, `STOCKTRNTRNDETAILNUMBER` | [`STOCKTRANSACTION`](../INVENTORY/STOCKTRANSACTION.md) | `COMPANYCODE`, `TRANSACTIONNUMBER`, `TRANSACTIONDETAILNUMBER` | RESTRICT | `PLANTINVOICETRANSACTION.PLANTINVOICECOMPANYCODE = STOCKTRANSACTION.COMPANYCODE AND PLANTINVOICETRANSACTION.STOCKTRNTRANSACTIONNUMBER = STOCKTRANSACTION.TRANSACTIONNUMBER AND PLANTINVOICETRANSACTION.STOCKTRNTRNDETAILNUMBER = STOCKTRANSACTION.TRANSACTIONDETAILNUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PLANTINVOICETRANSACTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PLANTINVOICECOMPANYCODE,
       t.PLANTINVOICEDIVISIONCODE,
       t.PLANTINVOICECODE,
       t.STOCKTRNTRANSACTIONNUMBER,
       t.STOCKTRNTRNDETAILNUMBER,
       t.INVOICELINENO,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.PLANTINVOICETRANSACTION t
FETCH FIRST 100 ROWS ONLY;
```
