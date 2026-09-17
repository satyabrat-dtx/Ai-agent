# DB2ADMIN.WRKFINOUTSTANDINGBALANCEAUDIT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 239345

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 4 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 5 | `DOCUMENTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 6 | `STATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 7 | `CODE` | CHAR(15) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 8 | `LINENUMBER` | DECIMAL(7,0) |  |  |  |  |
| 9 | `REVERSED` | SMALLINT | NOT NULL |  |  |  |
| 10 | `TDSCHECK` | SMALLINT | NOT NULL |  |  |  |
| 11 | `CRTOCR` | SMALLINT | NOT NULL |  |  |  |
| 12 | `DRTODR` | SMALLINT | NOT NULL |  |  |  |
| 13 | `ORDERPARTNERTYPE` | CHAR(1) |  |  |  |  |
| 14 | `ORDERPARTNERCODE` | CHAR(8) |  |  |  |  |
| 15 | `GLCODE` | CHAR(20) |  |  |  |  |
| 16 | `AMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 17 | `AMOUNTINDC` | DECIMAL(18,5) |  |  |  |  |
| 18 | `CLEAREDAMOUNTINCC` | DECIMAL(18,5) |  |  |  |  |
| 19 | `BALANCEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 20 | `DIFFERENCEAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINOUTSTANDINGBLNAUDITUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.COMPANYCODE,
       t.BUSINESSUNITCODE,
       t.FINANCIALYEARCODE,
       t.DOCUMENTTEMPLATECODE,
       t.STATISTICALGROUPCODE,
       t.CODE,
       t.LINENUMBER,
       t.REVERSED,
       t.TDSCHECK,
       t.CRTOCR
FROM   DB2ADMIN.WRKFINOUTSTANDINGBALANCEAUDIT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
