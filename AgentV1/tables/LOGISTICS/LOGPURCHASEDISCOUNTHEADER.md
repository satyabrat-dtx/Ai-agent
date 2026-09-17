# DB2ADMIN.LOGPURCHASEDISCOUNTHEADER

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 27
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 116775

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURCHASEPRICELISTCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PURCHASEPRICELISTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `LINEID` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 3 | `INITIALDATE` | DATE |  |  |  |  |
| 4 | `FINALDATE` | DATE |  |  |  |  |
| 5 | `PAYMENTMETHODCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `PAYMENTMETHODCODE` | CHAR(3) |  |  |  |  |
| 7 | `DISCOUNTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 8 | `VALUE` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 9 | `DISCOUNTCURRENCYCODE` | CHAR(4) |  |  |  |  |
| 10 | `SIGN` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `TAXAPPLICATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `CALCULATIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 13 | `AMOUNTCALCULATIONTYPE` | CHAR(2) |  |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 20 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 21 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 22 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 23 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 24 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 25 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 26 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPURCHASEDISCOUNTHEADER.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.PURCHASEPRICELISTCOMPANYCODE,
       t.PURCHASEPRICELISTCODE,
       t.LINEID,
       t.INITIALDATE,
       t.FINALDATE,
       t.PAYMENTMETHODCOMPANYCODE,
       t.PAYMENTMETHODCODE,
       t.DISCOUNTTYPE,
       t.VALUE,
       t.DISCOUNTCURRENCYCODE,
       t.SIGN,
       t.TAXAPPLICATIONTYPE
FROM   DB2ADMIN.LOGPURCHASEDISCOUNTHEADER t
FETCH FIRST 100 ROWS ONLY;
```
