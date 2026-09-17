# DB2ADMIN.LOGPURCHASEPRICEDETAIL

- **Module**: `LOGISTICS` (high confidence — table name starts with 'LOG')
- **Roles**: `change_log`, `child_of_implicit_parent`
- **Columns**: 22
- **Primary key**: `ABSUNIQUEID`, `LOGTIMESTAMP`, `UUID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 116823

> Row-level change-log/audit table.

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURPRCLINEPURPRCLISTCMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 1 | `PURPRCLINEPURPRICELISTCODE` | CHAR(8) | NOT NULL |  |  |  |
| 2 | `PURCHASEPRICELINELINEID` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 3 | `NUMBERLINEID` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 4 | `BREAKDOWNINITIALLIMIT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 5 | `BREAKDOWNLIMIT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 6 | `PRICETYPE` | CHAR(2) | NOT NULL |  |  |  |
| 7 | `PRICE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `PRICEINCLUDINGTAX` | SMALLINT | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL | PK | primary_key surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `LOGTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit | When the audited change was recorded (change-log table). |
| 15 | `LOGOPERATION` | INTEGER | NOT NULL |  | audit | Kind of audited change -- insert/update/delete (change-log table). |
| 16 | `LOGUSER` | CHAR(50) |  |  | audit | User responsible for the audited change (change-log table). |
| 17 | `UUID` | VARCHAR(50) | NOT NULL | PK | primary_key | Externally-generated unique identifier, used for integration correlation. |
| 18 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `LOGUPDATEDFIELDS` | CLOB(1000000) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `LOGPURCHASEPRICEDETAIL.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Starter query

```sql
SELECT t.PURPRCLINEPURPRCLISTCMYCODE,
       t.PURPRCLINEPURPRICELISTCODE,
       t.PURCHASEPRICELINELINEID,
       t.NUMBERLINEID,
       t.BREAKDOWNINITIALLIMIT,
       t.BREAKDOWNLIMIT,
       t.PRICETYPE,
       t.PRICE,
       t.PRICEINCLUDINGTAX,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.LOGPURCHASEPRICEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
