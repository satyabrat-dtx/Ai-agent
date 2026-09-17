# DB2ADMIN.WRKRULETEMPLATE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 41930

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `TEMPLATECODE` | CHAR(3) |  |  |  |  |
| 5 | `ISHEADER` | SMALLINT | NOT NULL |  |  |  |
| 6 | `ENTITYTYPE` | INTEGER | NOT NULL |  |  |  |
| 7 | `ENTITYCODE` | CHAR(3) |  |  |  |  |
| 8 | `ENTITYLABEL` | CHAR(50) | NOT NULL |  |  |  |
| 9 | `ADENTITYNAME` | CHAR(50) |  |  |  |  |
| 10 | `ADDATANAME` | CHAR(50) |  |  |  |  |
| 11 | `ADFIELDNAME` | VARCHAR(120) |  |  |  |  |
| 12 | `ABSUIXMLABSUIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 13 | `ABSUIXMLABSUIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 14 | `ABSUIXMLNAME` | VARCHAR(120) |  |  |  |  |
| 15 | `IDENTIFIER` | DECIMAL(4,0) |  |  |  |  |
| 16 | `SEQUENCE` | DECIMAL(5,0) |  |  |  |  |
| 17 | `LABEL` | CHAR(120) |  |  |  |  |
| 18 | `ATTRIBUTETYPE` | CHAR(2) |  |  |  |  |
| 19 | `ATTRIBUTETYPEVALUE` | INTEGER | NOT NULL |  |  |  |
| 20 | `OUTPUTENTITYCODE` | CHAR(3) |  |  |  |  |
| 21 | `OUTPUTABSUIXMLABSUIXMLPATH` | VARCHAR(50) |  |  |  |  |
| 22 | `OUTPUTABSUIXMLABSUIXMLNAME` | VARCHAR(54) |  |  |  |  |
| 23 | `OUTPUTABSUIXMLNAME` | VARCHAR(120) |  |  |  |  |
| 24 | `USERDEFINEDID` | CHAR(50) |  |  |  |  |
| 25 | `COMPAREOPERATOR` | INTEGER | NOT NULL |  |  |  |
| 26 | `LIKEINIT` | INTEGER | NOT NULL |  |  |  |
| 27 | `LIKELENGTH` | INTEGER | NOT NULL |  |  |  |
| 28 | `RANGEIDENTIFIER` | DECIMAL(3,0) |  |  |  |  |
| 29 | `REALREFERENCED` | VARCHAR(100) |  |  |  |  |
| 30 | `OUTPUTTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 31 | `OUTPUTIDENTIFIER` | DECIMAL(4,0) |  |  |  |  |
| 32 | `CANNOTBEEMPTY` | SMALLINT | NOT NULL |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.COMPANYCODE,
       t.TEMPLATECODE,
       t.ISHEADER,
       t.ENTITYTYPE,
       t.ENTITYCODE,
       t.ENTITYLABEL,
       t.ADENTITYNAME,
       t.ADDATANAME,
       t.ADFIELDNAME
FROM   DB2ADMIN.WRKRULETEMPLATE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
