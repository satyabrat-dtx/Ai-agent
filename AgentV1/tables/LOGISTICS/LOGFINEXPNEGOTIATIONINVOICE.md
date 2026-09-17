# DB2ADMIN.LOGFINEXPNEGOTIATIONINVOICE

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 34
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 202881

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NEGOTIATIONCODE` | CHAR(10) | NOT NULL |  |  |  |
| 2 | `INVOICEDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `INVOICECODE` | CHAR(20) | NOT NULL |  |  |  |
| 4 | `CUSTOMERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 5 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `FCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `INRVALUE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `INVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 10 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 11 | `FINDOCUMENTDATE` | DATE |  |  |  |  |
| 12 | `SHIPMENTDATE` | DATE |  |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 20 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 21 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 22 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 23 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 24 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 25 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 26 | `INVOICEVALUECC` | DECIMAL(18,5) |  |  |  |  |
| 27 | `LINENO` | INTEGER | NOT NULL |  |  |  |
| 28 | `RECEIVEDVALUEINFGN` | DECIMAL(18,5) |  |  |  |  |
| 29 | `RECEIVEDVALUEININR` | DECIMAL(18,5) |  |  |  |  |
| 30 | `CLAIMFGN` | DECIMAL(18,5) |  |  |  |  |
| 31 | `BANKCHARGESFGN` | DECIMAL(18,5) |  |  |  |  |
| 32 | `TOTALUSEDVALUE` | DECIMAL(18,5) |  |  |  |  |
| 33 | `BALANCEINVVALUE` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINEXPNEGOTIATION**.`ABSUNIQUEID` (medium confidence — name = 'LOGFINEXPNEGOTIATION' + recurring fragment 'INVOICE' (seen in 28 tables))
  - JOIN predicate: `LOGFINEXPNEGOTIATIONINVOICE.FATHERID = LOGFINEXPNEGOTIATION.ABSUNIQUEID`

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NEGOTIATIONCODE,
       t.INVOICEDIVISIONCODE,
       t.INVOICECODE,
       t.CUSTOMERCUSTOMERSUPPLIERTYPE,
       t.CUSTOMERCUSTOMERSUPPLIERCODE,
       t.ITEMTYPECODE,
       t.FCVALUE,
       t.INRVALUE,
       t.INVOICEVALUE,
       t.CURRENCYCODE,
       t.FINDOCUMENTDATE
FROM   DB2ADMIN.LOGFINEXPNEGOTIATIONINVOICE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
