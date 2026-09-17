# DB2ADMIN.PURCHASEORDERLINECOMMENT

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `PURORDLINEPURORDERCOMPANYCODE`, `PURORDLINEPURORDERCOUNTERCODE`, `PURORDERLINEPURCHASEORDERCODE`, `PURCHASEORDERLINEORDERLINE`, `PURCHASEORDERLINEORDERSUBLINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 2127

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PURORDLINEPURORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PURORDLINEPURORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PURORDERLINEPURCHASEORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PURCHASEORDERLINEORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PURCHASEORDERLINEORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 6 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 7 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 9 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 10 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 11 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PURCHASEORDERLINE_COMMENT` | `PURORDLINEPURORDERCOMPANYCODE`, `PURORDLINEPURORDERCOUNTERCODE`, `PURORDERLINEPURCHASEORDERCODE`, `PURCHASEORDERLINEORDERLINE`, `PURCHASEORDERLINEORDERSUBLINE` | [`PURCHASEORDERLINE`](../PURCHASING/PURCHASEORDERLINE.md) | `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE`, `ORDERLINE`, `ORDERSUBLINE` | RESTRICT | `PURCHASEORDERLINECOMMENT.PURORDLINEPURORDERCOMPANYCODE = PURCHASEORDERLINE.PURCHASEORDERCOMPANYCODE AND PURCHASEORDERLINECOMMENT.PURORDLINEPURORDERCOUNTERCODE = PURCHASEORDERLINE.PURCHASEORDERCOUNTERCODE AND PURCHASEORDERLINECOMMENT.PURORDERLINEPURCHASEORDERCODE = PURCHASEORDERLINE.PURCHASEORDERCODE AND PURCHASEORDERLINECOMMENT.PURCHASEORDERLINEORDERLINE = PURCHASEORDERLINE.ORDERLINE AND PURCHASEORDERLINECOMMENT.PURCHASEORDERLINEORDERSUBLINE = PURCHASEORDERLINE.ORDERSUBLINE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDERLINECOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PURORDLINEPURORDERCOMPANYCODE,
       t.PURORDLINEPURORDERCOUNTERCODE,
       t.PURORDERLINEPURCHASEORDERCODE,
       t.PURCHASEORDERLINEORDERLINE,
       t.PURCHASEORDERLINEORDERSUBLINE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED,
       t.ABSUNIQUEID
FROM   DB2ADMIN.PURCHASEORDERLINECOMMENT t
FETCH FIRST 100 ROWS ONLY;
```
