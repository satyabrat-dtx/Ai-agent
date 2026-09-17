# DB2ADMIN.STOCKTRANSACTIONORDERWORK

- **Module**: `INVENTORY` (high confidence — table name starts with 'STOCK')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 35699

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `ORDERCODE` | CHAR(15) |  |  |  |  |
| 6 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 7 | `ORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 8 | `ORDERCOMPONENTLINE` | DECIMAL(3,0) |  |  |  |  |
| 9 | `ORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 10 | `DERIVATIONCODE` | CHAR(15) |  |  |  |  |
| 11 | `DERIVATIONLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 12 | `DERIVATIONCOMPONENTLINENUMBER` | DECIMAL(5,0) |  |  |  |  |
| 13 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 14 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 15 | `STOCKTRANSACTIONTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 16 | `GBERROR` | BLOB(1000000) |  |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `ORDERCOUNTERCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `STOCKTRANSACTIONORDERWORKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.ORDERCOUNTERCODE,
       t.ORDERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.ORDERCOMPONENTLINE,
       t.ORDERDELIVERYLINE,
       t.DERIVATIONCODE,
       t.DERIVATIONLINENUMBER
FROM   DB2ADMIN.STOCKTRANSACTIONORDERWORK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
