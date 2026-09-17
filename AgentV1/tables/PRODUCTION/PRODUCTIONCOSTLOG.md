# DB2ADMIN.PRODUCTIONCOSTLOG

- **Module**: `PRODUCTION` (high confidence — table name starts with 'PRODUCTION')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `CHANGENUMBER`
- **FK degree**: referenced by 2 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 44191

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CHANGENUMBER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 2 | `COUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 3 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `CHANGEDENTITY` | CHAR(1) |  |  |  |  |
| 5 | `DEMANDCHANGE` | CHAR(1) |  |  |  |  |
| 6 | `STEPCHANGE` | CHAR(1) |  |  |  |  |
| 7 | `RESERVATIONCHANGE` | CHAR(1) |  |  |  |  |
| 8 | `STEPNUMBER` | DECIMAL(5,0) |  |  |  |  |
| 9 | `RESERVATIONLINE` | DECIMAL(7,0) |  |  |  |  |
| 10 | `DEMANDPROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 11 | `COUNTERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COUNTER_COUNTER` | `COUNTERCOMPANYCODE`, `COUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PRODUCTIONCOSTLOG.COUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND PRODUCTIONCOSTLOG.COUNTERCODE = COUNTER.CODE` |

## Referenced by (child → this table) — 2

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PRODUCTIONCOSTLOG_RESERVATION` | [`PRODUCTIONRESERVATIONCOSTLOG`](../PRODUCTION/PRODUCTIONRESERVATIONCOSTLOG.md) | `PRODUCTIONCOSTLOGCOMPANYCODE`, `PRODUCTIONCOSTLOGCHANGENUMBER` | `PRODUCTIONRESERVATIONCOSTLOG.PRODUCTIONCOSTLOGCOMPANYCODE = PRODUCTIONCOSTLOG.COMPANYCODE AND PRODUCTIONRESERVATIONCOSTLOG.PRODUCTIONCOSTLOGCHANGENUMBER = PRODUCTIONCOSTLOG.CHANGENUMBER` |
| `PRODUCTIONCOSTLOG_STEP` | [`PRODUCTIONSTEPCOSTLOG`](../PRODUCTION/PRODUCTIONSTEPCOSTLOG.md) | `PRODUCTIONCOSTLOGCOMPANYCODE`, `PRODUCTIONCOSTLOGCHANGENUMBER` | `PRODUCTIONSTEPCOSTLOG.PRODUCTIONCOSTLOGCOMPANYCODE = PRODUCTIONCOSTLOG.COMPANYCODE AND PRODUCTIONSTEPCOSTLOG.PRODUCTIONCOSTLOGCHANGENUMBER = PRODUCTIONCOSTLOG.CHANGENUMBER` |

## Indexes

- `PRODUCTIONCOSTLOGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CHANGENUMBER,
       t.COUNTERCODE,
       t.CODE,
       t.CHANGEDENTITY,
       t.DEMANDCHANGE,
       t.STEPCHANGE,
       t.RESERVATIONCHANGE,
       t.STEPNUMBER,
       t.RESERVATIONLINE,
       t.DEMANDPROGRESSSTATUS,
       t.COUNTERCOMPANYCODE
FROM   DB2ADMIN.PRODUCTIONCOSTLOG t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
