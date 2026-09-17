# DB2ADMIN.WRKSALESCLAIMRETURN

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 30
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 93113

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `STOCKTRNTRANSACTIONNUMBER` | CHAR(15) |  |  |  |  |
| 5 | `STOCKTRNTRNDETAILNUMBER` | INTEGER | NOT NULL |  |  |  |
| 6 | `ORIGORDERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 7 | `ORIGORDERLINE` | DECIMAL(7,0) | NOT NULL |  |  |  |
| 8 | `ORIGORDERDETAILLINE` | DECIMAL(3,0) | NOT NULL |  |  |  |
| 9 | `DOCLINELOGICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 10 | `SIGNEDPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `SGNUSERPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 12 | `SIGNEDSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 13 | `SGNUSERSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 14 | `SIGNEDPACKAGINGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 15 | `SGNUSERPACKAGINGUOMCODE` | CHAR(3) |  |  |  |  |
| 16 | `WRKLOTCODE` | CHAR(35) |  |  |  |  |
| 17 | `WRKCNRITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 18 | `WRKCONTAINERITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 19 | `WRKCONTAINERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 20 | `WRKCONTAINERSUBCODE01` | CHAR(20) |  |  |  |  |
| 21 | `WRKCONTAINERELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 22 | `WRKCONTAINERELEMENTCODE` | CHAR(15) |  |  |  |  |
| 23 | `WRKITEMELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 24 | `WRKITEMELEMENTCODE` | CHAR(15) |  |  |  |  |
| 25 | `WRKPHYWAREHOUSECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 26 | `WRKPHYSICALWAREHOUSECODE` | CHAR(8) |  |  |  |  |
| 27 | `WRKWHSLOCWHSZONEPHYWHSCMYCODE` | CHAR(3) |  |  |  |  |
| 28 | `WRKWHSLOCWAREHOUSEZONECODE` | CHAR(3) |  |  |  |  |
| 29 | `WRKWHSLOCCODE` | CHAR(10) |  |  |  |  |

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
       t.STOCKTRNTRANSACTIONNUMBER,
       t.STOCKTRNTRNDETAILNUMBER,
       t.ORIGORDERCODE,
       t.ORIGORDERLINE,
       t.ORIGORDERDETAILLINE,
       t.DOCLINELOGICALWAREHOUSECODE,
       t.SIGNEDPRIMARYQUANTITY,
       t.SGNUSERPRIMARYUOMCODE
FROM   DB2ADMIN.WRKSALESCLAIMRETURN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
