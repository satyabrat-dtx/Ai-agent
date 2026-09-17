# DB2ADMIN.WRKFATHERCHILDBOM

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 76
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 193225

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `WRKFATHERCHILDPRODUCTLINE` | INTEGER | NOT NULL |  |  |  |
| 4 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 6 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 7 | `SOURCEBOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 8 | `SOURCEBOMCODE` | VARCHAR(120) |  |  |  |  |
| 9 | `NEWBOMDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 10 | `NEWBOMALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 11 | `NEWBOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 12 | `NEWBOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 13 | `NEWBOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 14 | `NEWBOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 15 | `NEWBOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 16 | `NEWBOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 17 | `NEWBOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 18 | `NEWBOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 19 | `NEWBOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 20 | `NEWBOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 21 | `NEWBOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 22 | `NEWBOMLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 23 | `NEWBOMRESETREFBOMLINK` | SMALLINT | NOT NULL |  |  |  |
| 24 | `NEWBOMBOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 25 | `NEWBOMBOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 26 | `NEWBOMBOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 27 | `NEWBOMBOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 28 | `NEWBOMBOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 29 | `NEWBOMBOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 30 | `NEWBOMBOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 31 | `NEWBOMBOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 32 | `NEWBOMBOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 33 | `NEWBOMBOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 34 | `NEWBOMREFBOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 35 | `NEWBOMREFBOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 36 | `NEWBOMPRODUCTIONBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 37 | `NEWBOMPRODBOMSTARTDATE` | DATE |  |  |  |  |
| 38 | `NEWBOMPRODBOMENDDATE` | DATE |  |  |  |  |
| 39 | `NEWBOMPRODUCTIONREFERENCEBOM` | SMALLINT | NOT NULL |  |  |  |
| 40 | `NEWBOMPRODREFBOMSTARTDATE` | DATE |  |  |  |  |
| 41 | `NEWBOMPRODREFBOMENDDATE` | DATE |  |  |  |  |
| 42 | `NEWBOMCOSTCLCBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 43 | `NEWBOMCOSTCALCBOMSTARTDATE` | DATE |  |  |  |  |
| 44 | `NEWBOMCOSTCALCBOMENDDATE` | DATE |  |  |  |  |
| 45 | `NEWBOMTECHNICALBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 46 | `NEWBOMTECHBOMSTARTDATE` | DATE |  |  |  |  |
| 47 | `NEWBOMTECHBOMENDDATE` | DATE |  |  |  |  |
| 48 | `NEWBOMPLANNINGBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 49 | `NEWBOMPLANBOMSTARTDATE` | DATE |  |  |  |  |
| 50 | `NEWBOMPLANBOMENDDATE` | DATE |  |  |  |  |
| 51 | `NEWBOMBOMTYPECODE` | CHAR(6) |  |  |  |  |
| 52 | `NEWBOMCHECKCODE` | CHAR(2) |  |  |  |  |
| 53 | `NEWBOMUSERGENGRPTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 54 | `NEWBOMUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 55 | `NEWBOMGENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 56 | `NEWBOMPLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 57 | `NEWBOMPLANTCODE` | CHAR(8) |  |  |  |  |
| 58 | `NEWBOMCOSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 59 | `NEWBOMSTCGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 60 | `NEWBOMSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 61 | `NEWBOMCOLLECTIONGRPCMYCODE` | CHAR(3) |  |  |  |  |
| 62 | `NEWBOMCOLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 63 | `NEWBOMBOMUOMTYPE` | CHAR(2) |  |  |  |  |
| 64 | `NEWBOMBOMUOMCODE` | CHAR(3) |  |  |  |  |
| 65 | `NEWBOMBOMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 66 | `NEWBOMBOMINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 67 | `NEWBOMBOMCOMMENTCRITERIA` | CHAR(2) |  |  |  |  |
| 68 | `NEWBOMHEADERCOMMENTPOLICYCODE` | CHAR(20) |  |  |  |  |
| 69 | `NEWBOMCOMMENTCHOOSEKEYSTYPE` | CHAR(1) |  |  |  |  |
| 70 | `NEWBOMCOMMENTCHOOSEKEYSCODE` | CHAR(3) |  |  |  |  |
| 71 | `NEWBOMSTATUS` | CHAR(1) | NOT NULL |  |  |  |
| 72 | `NEWBOMRUNAPPROVE` | SMALLINT | NOT NULL |  |  |  |
| 73 | `NEWBOMRUNACTIVATE` | SMALLINT | NOT NULL |  |  |  |
| 74 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 75 | `SOURCEBOMCOMPANYCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CREATIONUSER,
       t.LINE,
       t.WRKFATHERCHILDPRODUCTLINE,
       t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SOURCEBOMNUMBERID,
       t.SOURCEBOMCODE,
       t.NEWBOMDIVISIONCODE,
       t.NEWBOMALLOWEDDIVISIONS,
       t.NEWBOMSUBCODE01
FROM   DB2ADMIN.WRKFATHERCHILDBOM t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
