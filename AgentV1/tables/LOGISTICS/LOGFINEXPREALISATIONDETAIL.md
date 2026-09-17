# DB2ADMIN.LOGFINEXPREALISATIONDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 50
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 224456

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINEXPREALISATIONCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `FINEXPREALISATIONCODE` | CHAR(15) | NOT NULL |  |  |  |
| 2 | `NEGOTIATIONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 3 | `NEGOTIATIONCODE` | CHAR(10) |  |  |  |  |
| 4 | `INVOICEDIVISIONCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `INVOICECODE` | CHAR(20) | NOT NULL |  |  |  |
| 6 | `CSMCSMSUPPLIERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `CUSTOMERCUSTOMERSUPPLIERTYPE` | CHAR(1) |  |  |  |  |
| 8 | `CUSTOMERCUSTOMERSUPPLIERCODE` | CHAR(8) |  |  |  |  |
| 9 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 10 | `INRVALUE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `INVOICEVALUE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `CURRENCYCODE` | CHAR(4) |  |  |  |  |
| 13 | `FINDOCUMENTDATE` | DATE |  |  |  |  |
| 14 | `SHIPMENTDATE` | DATE |  |  |  |  |
| 15 | `INVOICEDATE` | DATE |  |  |  |  |
| 16 | `OUTSTANDINGVALUE` | DECIMAL(18,5) |  |  |  |  |
| 17 | `RECIEPTINDC` | DECIMAL(18,5) |  |  |  |  |
| 18 | `RECEIPTININR` | DECIMAL(18,5) |  |  |  |  |
| 19 | `PROJECTDOCNO` | CHAR(20) |  |  |  |  |
| 20 | `PROJECTVALUE` | DECIMAL(18,5) |  |  |  |  |
| 21 | `CLAIMINDC` | DECIMAL(18,5) |  |  |  |  |
| 22 | `BANKCHARGESINDC` | DECIMAL(18,5) |  |  |  |  |
| 23 | `LEGALNAME1` | VARCHAR(200) |  |  |  |  |
| 24 | `DISCOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 25 | `LATESHIPMENTPENALTYINDC` | DECIMAL(18,5) |  |  |  |  |
| 26 | `SHORTSHIPMENTINDC` | DECIMAL(18,5) |  |  |  |  |
| 27 | `PRICEDIFFERENCEINDC` | DECIMAL(18,5) |  |  |  |  |
| 28 | `UPCHARGEINDC` | DECIMAL(18,5) |  |  |  |  |
| 29 | `BUYERAGENCYCOMMISSIONINDC` | DECIMAL(18,5) |  |  |  |  |
| 30 | `LCCHARGESINDC` | DECIMAL(18,5) |  |  |  |  |
| 31 | `EXCHANGERATEOFCONTRACT` | DECIMAL(18,5) |  |  |  |  |
| 32 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 33 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 34 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 35 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 36 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 37 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 38 | `BALANCEVALUEINDC` | DECIMAL(18,5) |  |  |  |  |
| 39 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 40 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 41 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 42 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 43 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 44 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 45 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |
| 46 | `RECOVERYFGN` | DECIMAL(18,5) |  |  |  |  |
| 47 | `RECOVERYDATE` | DATE |  |  |  |  |
| 48 | `REVERSEDVALUEINFGN` | DECIMAL(18,5) |  |  |  |  |
| 49 | `REVERSEDDATE` | DATE |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **LOGFINEXPREALISATION**.`ABSUNIQUEID` (high confidence — name = 'LOGFINEXPREALISATION' + known child suffix 'DETAIL')
  - JOIN predicate: `LOGFINEXPREALISATIONDETAIL.FATHERID = LOGFINEXPREALISATION.ABSUNIQUEID`

## Starter query

```sql
SELECT t.FINEXPREALISATIONCOMPANYCODE,
       t.FINEXPREALISATIONCODE,
       t.NEGOTIATIONCOMPANYCODE,
       t.NEGOTIATIONCODE,
       t.INVOICEDIVISIONCODE,
       t.INVOICECODE,
       t.CSMCSMSUPPLIERCOMPANYCODE,
       t.CUSTOMERCUSTOMERSUPPLIERTYPE,
       t.CUSTOMERCUSTOMERSUPPLIERCODE,
       t.ITEMTYPECODE,
       t.INRVALUE,
       t.INVOICEVALUE
FROM   DB2ADMIN.LOGFINEXPREALISATIONDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
