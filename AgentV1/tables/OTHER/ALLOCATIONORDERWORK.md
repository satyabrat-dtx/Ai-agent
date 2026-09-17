# DB2ADMIN.ALLOCATIONORDERWORK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 21
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 10142

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `DETAILTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 5 | `ORIGINTYPE` | CHAR(2) |  |  |  |  |
| 6 | `DESTINATIONTYPE` | CHAR(2) |  |  |  |  |
| 7 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 8 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 9 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 10 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 11 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 12 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 13 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 14 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 15 | `DERIVATIONCODE` | CHAR(15) |  |  |  |  |
| 16 | `DERIVATIONLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 17 | `DERIVATIONCOMPONENTLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 19 | `TEMPLATECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `ORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ALLOCATIONORDERWORKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.DETAILTYPE,
       t.ORIGINTYPE,
       t.DESTINATIONTYPE,
       t.TEMPLATECODE,
       t.CODE,
       t.ORDERCOUNTERCODE,
       t.ORDERCODE,
       t.ORDERLINE
FROM   DB2ADMIN.ALLOCATIONORDERWORK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
