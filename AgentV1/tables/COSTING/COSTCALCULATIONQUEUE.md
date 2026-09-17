# DB2ADMIN.COSTCALCULATIONQUEUE

- **Module**: `COSTING` (high confidence — table name starts with 'COST')
- **Roles**: `business_data`
- **Columns**: 17
- **Primary key**: `TABLEINDEX`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 24259

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TABLEINDEX` | BIGINT | NOT NULL | PK | primary_key |  |
| 1 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `PLANTCODE` | CHAR(8) |  |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 4 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 5 | `PRODUCTSUBCODE01` | CHAR(20) |  |  |  |  |
| 6 | `PRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 7 | `PRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 8 | `PRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 9 | `PRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 10 | `PRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 11 | `PRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 12 | `PRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 13 | `PRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 14 | `PRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 16 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `COSTCALCULATIONQUEUEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TABLEINDEX,
       t.COMPANYCODE,
       t.PLANTCODE,
       t.ITEMTYPECODE,
       t.PROGRESSSTATUS,
       t.PRODUCTSUBCODE01,
       t.PRODUCTSUBCODE02,
       t.PRODUCTSUBCODE03,
       t.PRODUCTSUBCODE04,
       t.PRODUCTSUBCODE05,
       t.PRODUCTSUBCODE06,
       t.PRODUCTSUBCODE07
FROM   DB2ADMIN.COSTCALCULATIONQUEUE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
