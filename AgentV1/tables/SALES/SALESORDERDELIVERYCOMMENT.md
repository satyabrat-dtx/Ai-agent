# DB2ADMIN.SALESORDERDELIVERYCOMMENT

- **Module**: `SALES` (high confidence — table name starts with 'SALESORDER')
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `COUNTERCODE`, `ORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE`, `SALESORDERDELIVERYDELIVERYLINE`, `ORIGIN`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 13624

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `COUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `COMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `SALESORDERDELIVERYDELIVERYLINE` | DECIMAL(3,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 7 | `REPORTTYPE` | CHAR(90) |  |  |  |  |
| 8 | `ORIGIN` | INTEGER | NOT NULL | PK | primary_key |  |
| 9 | `CODE` | CHAR(12) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 10 | `COMMENTTEXT` | LONG VARCHAR | NOT NULL |  |  |  |
| 11 | `COMMENTTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 12 | `CANCELED` | SMALLINT | NOT NULL |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 18 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 19 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `SALESORDERDELIVERY_COMMENT` | `COMPANYCODE`, `COUNTERCODE`, `ORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE`, `SALESORDERDELIVERYDELIVERYLINE` | [`SALESORDERDELIVERY`](../SALES/SALESORDERDELIVERY.md) | `SALORDLINESALORDERCOMPANYCODE`, `SALORDLINESALORDERCOUNTERCODE`, `SALESORDERLINESALESORDERCODE`, `SALESORDERLINEORDERLINE`, `SALESORDERLINEORDERSUBLINE`, `SALORDLINECOMPONENTORDERLINE`, `DELIVERYLINE` | RESTRICT | `SALESORDERDELIVERYCOMMENT.COMPANYCODE = SALESORDERDELIVERY.SALORDLINESALORDERCOMPANYCODE AND SALESORDERDELIVERYCOMMENT.COUNTERCODE = SALESORDERDELIVERY.SALORDLINESALORDERCOUNTERCODE AND SALESORDERDELIVERYCOMMENT.ORDERCODE = SALESORDERDELIVERY.SALESORDERLINESALESORDERCODE AND SALESORDERDELIVERYCOMMENT.ORDERLINE = SALESORDERDELIVERY.SALESORDERLINEORDERLINE AND SALESORDERDELIVERYCOMMENT.ORDERSUBLINE = SALESORDERDELIVERY.SALESORDERLINEORDERSUBLINE AND SALESORDERDELIVERYCOMMENT.COMPONENTORDERLINE = SALESORDERDELIVERY.SALORDLINECOMPONENTORDERLINE AND SALESORDERDELIVERYCOMMENT.SALESORDERDELIVERYDELIVERYLINE = SALESORDERDELIVERY.DELIVERYLINE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SALESORDERDELIVERYCOMMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.COUNTERCODE,
       t.ORDERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.COMPONENTORDERLINE,
       t.SALESORDERDELIVERYDELIVERYLINE,
       t.REPORTTYPE,
       t.ORIGIN,
       t.CODE,
       t.COMMENTTEXT,
       t.COMMENTTYPE
FROM   DB2ADMIN.SALESORDERDELIVERYCOMMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
