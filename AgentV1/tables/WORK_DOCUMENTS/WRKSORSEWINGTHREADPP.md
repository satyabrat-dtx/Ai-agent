# DB2ADMIN.WRKSORSEWINGTHREADPP

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 51
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 205571

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CHOOSER` | SMALLINT | NOT NULL |  |  |  |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `STEPNUMBER` | DECIMAL(5,0) | NOT NULL |  |  |  |
| 3 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `POWISEFLAG` | SMALLINT | NOT NULL |  |  |  |
| 5 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 6 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 8 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 10 | `PRODUCTIONORDERCOUNTERCODE` | CHAR(15) | NOT NULL |  |  |  |
| 11 | `PRODUCTIONORDERCODE` | CHAR(15) |  |  |  |  |
| 12 | `PRODUCTIONORDERDATE` | DATE |  |  |  |  |
| 13 | `PRODUCTIONDEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 14 | `PRODUCTIONDEMANDCODE` | CHAR(15) |  |  |  |  |
| 15 | `CURRENTSTEPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 16 | `ITEMCODE` | VARCHAR(200) |  |  |  |  |
| 17 | `POSTEPPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `POSTEPPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `POSTEPSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 20 | `POSTEPSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 21 | `PDSTEPPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 22 | `PDSTEPPRIMARYUOMCODE` | CHAR(3) |  |  |  |  |
| 23 | `PDSTEPSECONDARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 24 | `PDSTEPSECONDARYUOMCODE` | CHAR(3) |  |  |  |  |
| 25 | `PDSTEPPKGQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 26 | `PDSTEPPKGUOMCODE` | CHAR(3) |  |  |  |  |
| 27 | `ARTICLE` | CHAR(20) |  |  |  |  |
| 28 | `SHADECODE` | CHAR(10) |  |  |  |  |
| 29 | `CUSTOMER` | VARCHAR(200) |  |  |  |  |
| 30 | `CUSTOMERPO` | VARCHAR(200) |  |  |  |  |
| 31 | `CUSTOMERPODATE` | DATE |  |  |  |  |
| 32 | `USERQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 33 | `USERQUANTITYUOMCODE` | CHAR(3) |  |  |  |  |
| 34 | `PENDINGDAYS` | INTEGER | NOT NULL |  |  |  |
| 35 | `SHIFT` | INTEGER | NOT NULL |  |  |  |
| 36 | `RESOURCEMAINRESOURCECODE` | CHAR(8) |  |  |  |  |
| 37 | `RESOURCESHORTDESC` | VARCHAR(80) |  |  |  |  |
| 38 | `OPERATORGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 39 | `OPERATORGROUPCODE` | CHAR(3) |  |  |  |  |
| 40 | `OPERATOR1USERGEGPTYCMYCODE` | CHAR(3) |  |  |  |  |
| 41 | `OPERATOR1CODE` | CHAR(10) |  |  |  |  |
| 42 | `OPERATOR2USERGEGPTYCMYCODE` | CHAR(3) |  |  |  |  |
| 43 | `OPERATOR2CODE` | CHAR(10) |  |  |  |  |
| 44 | `CALCULATEDHOURS` | DECIMAL(15,5) |  |  |  |  |
| 45 | `UOMTYPE` | CHAR(1) |  |  |  |  |
| 46 | `INITIALUSERPRIMARYQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 47 | `CALCULATEDTIME3` | DECIMAL(10,5) |  |  |  |  |
| 48 | `NEXTACTION` | VARCHAR(100) |  |  |  |  |
| 49 | `HEADERDATA` | BLOB(1000000) |  |  |  |  |
| 50 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKSORSEWINGTHREADPPUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CHOOSER,
       t.CREATIONTIMESTAMP,
       t.STEPNUMBER,
       t.LINENO,
       t.POWISEFLAG,
       t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.PRODUCTIONORDERCOUNTERCODE,
       t.PRODUCTIONORDERCODE
FROM   DB2ADMIN.WRKSORSEWINGTHREADPP t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
