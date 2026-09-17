# DB2ADMIN.WRKLAYDOWNDOCUMENTCREATOR

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 105931

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `LINETOEXPLODE` | INTEGER | NOT NULL |  |  |  |
| 5 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 6 | `RESERVATIONGROUPLINE` | INTEGER | NOT NULL |  |  |  |
| 7 | `MARKERCODE` | CHAR(10) |  |  |  |  |
| 8 | `USERNOLAYERS` | INTEGER | NOT NULL |  |  |  |
| 9 | `MAXNOLAYERS` | INTEGER | NOT NULL |  |  |  |
| 10 | `MAXLAYLENGTH` | DECIMAL(8,3) | NOT NULL |  |  |  |
| 11 | `USERLAYLENGTH` | DECIMAL(8,3) | NOT NULL |  |  |  |
| 12 | `WIDTHRANGEFROM` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 13 | `WIDTHRANGETO` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 14 | `USERWIDTHRANGEFROM` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 15 | `USERWIDTHRANGETO` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 16 | `EXTERNALCODE` | CHAR(10) |  |  |  |  |
| 17 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 18 | `ITEMDETAILS` | CHAR(140) |  |  |  |  |
| 19 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 21 | `CHOOSED` | SMALLINT | NOT NULL |  |  |  |

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
       t.LINETOEXPLODE,
       t.PRODUCTIONORDERCODE,
       t.RESERVATIONGROUPLINE,
       t.MARKERCODE,
       t.USERNOLAYERS,
       t.MAXNOLAYERS,
       t.MAXLAYLENGTH,
       t.USERLAYLENGTH
FROM   DB2ADMIN.WRKLAYDOWNDOCUMENTCREATOR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
