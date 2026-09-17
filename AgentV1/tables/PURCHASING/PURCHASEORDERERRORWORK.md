# DB2ADMIN.PURCHASEORDERERRORWORK

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 11916

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ORIGINTYPE` | CHAR(2) | NOT NULL |  |  |  |
| 5 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 6 | `PURCHASEORDERCODE` | CHAR(15) |  |  |  |  |
| 7 | `ASSORTMENTNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 8 | `OPENORDPURORDLINEPURORDCNTCOD` | CHAR(8) |  |  |  |  |
| 9 | `OPENORDPURORDLINEPURORDERCODE` | CHAR(15) |  |  |  |  |
| 10 | `OPENORDPURORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 11 | `OPENORDPURORDLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 12 | `OPENORDERDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDERERRORWORKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.ORIGINTYPE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.ASSORTMENTNUMBERID,
       t.OPENORDPURORDLINEPURORDCNTCOD,
       t.OPENORDPURORDLINEPURORDERCODE,
       t.OPENORDPURORDERLINEORDERLINE,
       t.OPENORDPURORDLINEORDERSUBLINE
FROM   DB2ADMIN.PURCHASEORDERERRORWORK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
