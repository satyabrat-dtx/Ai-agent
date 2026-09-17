# DB2ADMIN.WRKCUTTINGHEADERCREATOR

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 105881

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `LAYDOWNDOCUMENTCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 5 | `LAYDOWNDOCUMENTCODE` | CHAR(15) |  |  |  |  |
| 6 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 7 | `RESERVATIONGROUPLINE` | INTEGER | NOT NULL |  |  |  |
| 8 | `MARKERCODE` | CHAR(10) |  |  |  |  |
| 9 | `FINALLAYERUSE` | INTEGER | NOT NULL |  |  |  |
| 10 | `USERNOLAYERS` | INTEGER | NOT NULL |  |  |  |
| 11 | `MAXNOLAYERS` | INTEGER | NOT NULL |  |  |  |
| 12 | `MAXLAYLENGTH` | DECIMAL(8,3) | NOT NULL |  |  |  |
| 13 | `USERLAYLENGTH` | DECIMAL(8,3) | NOT NULL |  |  |  |
| 14 | `WIDTHRANGEFROM` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 15 | `WIDTHRANGETO` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 16 | `USERWIDTHRANGEFROM` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 17 | `USERWIDTHRANGETO` | DECIMAL(5,2) | NOT NULL |  |  |  |
| 18 | `EXTERNALCODE` | CHAR(10) |  |  |  |  |
| 19 | `ITEMCODE` | VARCHAR(120) |  |  |  |  |
| 20 | `ITEMDETAILS` | CHAR(140) |  |  |  |  |
| 21 | `SIZECODE` | CHAR(10) |  |  |  |  |
| 22 | `QUANTITY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 23 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) |  |  |  |  |
| 24 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 25 | `CHOOSED` | SMALLINT | NOT NULL |  |  |  |
| 26 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 27 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 28 | `NUMBEROFBUNDLES` | INTEGER | NOT NULL |  |  |  |
| 29 | `ORDERLINE` | DECIMAL(7,0) |  |  |  |  |

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
       t.LAYDOWNDOCUMENTCOUNTERCODE,
       t.LAYDOWNDOCUMENTCODE,
       t.PRODUCTIONORDERCODE,
       t.RESERVATIONGROUPLINE,
       t.MARKERCODE,
       t.FINALLAYERUSE,
       t.USERNOLAYERS,
       t.MAXNOLAYERS
FROM   DB2ADMIN.WRKCUTTINGHEADERCREATOR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
