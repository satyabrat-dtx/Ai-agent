# DB2ADMIN.PURCHASEORDERDELIVERYCOMMENT

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `ORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `PURORDERDELIVERYDELIVERYLINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 19622

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PURORDERDELIVERYDELIVERYLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 7 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 8 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 10 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 11 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PURCHASEORDERDELIVERY_COMMENT` | `COMPANYCODE`, `COUNTERCODE`, `ORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `PURORDERDELIVERYDELIVERYLINE` | [`PURCHASEORDERDELIVERY`](../PURCHASING/PURCHASEORDERDELIVERY.md) | `PURORDLINEPURORDERCOMPANYCODE`, `PURORDLINEPURORDERCOUNTERCODE`, `PURORDERLINEPURCHASEORDERCODE`, `PURCHASEORDERLINEORDERLINE`, `PURCHASEORDERLINEORDERSUBLINE`, `DELIVERYLINE` | RESTRICT | `PURCHASEORDERDELIVERYCOMMENT.COMPANYCODE = PURCHASEORDERDELIVERY.PURORDLINEPURORDERCOMPANYCODE AND PURCHASEORDERDELIVERYCOMMENT.COUNTERCODE = PURCHASEORDERDELIVERY.PURORDLINEPURORDERCOUNTERCODE AND PURCHASEORDERDELIVERYCOMMENT.ORDERCODE = PURCHASEORDERDELIVERY.PURORDERLINEPURCHASEORDERCODE AND PURCHASEORDERDELIVERYCOMMENT.ORDERLINE = PURCHASEORDERDELIVERY.PURCHASEORDERLINEORDERLINE AND PURCHASEORDERDELIVERYCOMMENT.ORDERSUBLINE = PURCHASEORDERDELIVERY.PURCHASEORDERLINEORDERSUBLINE AND PURCHASEORDERDELIVERYCOMMENT.PURORDERDELIVERYDELIVERYLINE = PURCHASEORDERDELIVERY.DELIVERYLINE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURORDERDELIVERYCOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCODE,
       t.ORDERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.PURORDERDELIVERYDELIVERYLINE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE,
       t.CANCELED
FROM   DB2ADMIN.PURCHASEORDERDELIVERYCOMMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
