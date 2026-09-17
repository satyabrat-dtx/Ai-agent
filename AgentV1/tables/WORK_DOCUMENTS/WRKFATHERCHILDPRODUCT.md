# DB2ADMIN.WRKFATHERCHILDPRODUCT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 89
- **Primary key**: `CREATIONTIMESTAMP`, `LINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 193451

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 2 | `LINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 6 | `PRODUCTITEMCODE` | VARCHAR(120) |  |  |  |  |
| 7 | `PRODUCTSUBCODE01` | CHAR(20) |  |  |  |  |
| 8 | `PRODUCTSUBCODE02` | CHAR(10) |  |  |  |  |
| 9 | `PRODUCTSUBCODE03` | CHAR(10) |  |  |  |  |
| 10 | `PRODUCTSUBCODE04` | CHAR(10) |  |  |  |  |
| 11 | `PRODUCTSUBCODE05` | CHAR(10) |  |  |  |  |
| 12 | `PRODUCTSUBCODE06` | CHAR(10) |  |  |  |  |
| 13 | `PRODUCTSUBCODE07` | CHAR(10) |  |  |  |  |
| 14 | `PRODUCTSUBCODE08` | CHAR(10) |  |  |  |  |
| 15 | `PRODUCTSUBCODE09` | CHAR(10) |  |  |  |  |
| 16 | `PRODUCTSUBCODE10` | CHAR(10) |  |  |  |  |
| 17 | `FILTERBOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 18 | `FILTERBOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 19 | `FILTERBOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 20 | `FILTERBOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 21 | `FILTERBOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 22 | `FILTERBOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 23 | `FILTERBOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 24 | `FILTERBOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 25 | `FILTERBOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 26 | `FILTERBOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 27 | `FILTERBOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 28 | `FILTERBOMCODE` | VARCHAR(120) |  |  |  |  |
| 29 | `NEWBOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 30 | `NEWBOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 31 | `NEWBOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 32 | `NEWBOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 33 | `NEWBOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 34 | `NEWBOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 35 | `NEWBOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 36 | `NEWBOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 37 | `NEWBOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 38 | `NEWBOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 39 | `NEWBOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 40 | `NEWBOMLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 41 | `NEWBOMBOMSUBCODE01` | CHAR(20) |  |  |  |  |
| 42 | `NEWBOMBOMSUBCODE02` | CHAR(10) |  |  |  |  |
| 43 | `NEWBOMBOMSUBCODE03` | CHAR(10) |  |  |  |  |
| 44 | `NEWBOMBOMSUBCODE04` | CHAR(10) |  |  |  |  |
| 45 | `NEWBOMBOMSUBCODE05` | CHAR(10) |  |  |  |  |
| 46 | `NEWBOMBOMSUBCODE06` | CHAR(10) |  |  |  |  |
| 47 | `NEWBOMBOMSUBCODE07` | CHAR(10) |  |  |  |  |
| 48 | `NEWBOMBOMSUBCODE08` | CHAR(10) |  |  |  |  |
| 49 | `NEWBOMBOMSUBCODE09` | CHAR(10) |  |  |  |  |
| 50 | `NEWBOMBOMSUBCODE10` | CHAR(10) |  |  |  |  |
| 51 | `NEWBOMREFBOMSUFFIXCODE` | CHAR(20) |  |  |  |  |
| 52 | `NEWBOMREFBOMNUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 53 | `NEWBOMPRODUCTIONBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 54 | `NEWBOMPRODBOMSTARTDATE` | DATE |  |  |  |  |
| 55 | `NEWBOMPRODBOMENDDATE` | DATE |  |  |  |  |
| 56 | `NEWBOMPRODUCTIONREFERENCEBOM` | SMALLINT | NOT NULL |  |  |  |
| 57 | `NEWBOMPRODREFBOMSTARTDATE` | DATE |  |  |  |  |
| 58 | `NEWBOMPRODREFBOMENDDATE` | DATE |  |  |  |  |
| 59 | `NEWBOMCOSTCLCBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 60 | `NEWBOMCOSTCALCBOMSTARTDATE` | DATE |  |  |  |  |
| 61 | `NEWBOMCOSTCALCBOMENDDATE` | DATE |  |  |  |  |
| 62 | `NEWBOMTECHNICALBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 63 | `NEWBOMTECHBOMSTARTDATE` | DATE |  |  |  |  |
| 64 | `NEWBOMTECHBOMENDDATE` | DATE |  |  |  |  |
| 65 | `NEWBOMPLANNINGBOMMANAGEMENT` | SMALLINT | NOT NULL |  |  |  |
| 66 | `NEWBOMPLANBOMSTARTDATE` | DATE |  |  |  |  |
| 67 | `NEWBOMPLANBOMENDDATE` | DATE |  |  |  |  |
| 68 | `NEWBOMBOMTYPECODE` | CHAR(6) |  |  |  |  |
| 69 | `NEWBOMCHECKCODE` | CHAR(2) |  |  |  |  |
| 70 | `NEWBOMUSERGENGRPTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 71 | `NEWBOMUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 72 | `NEWBOMGENERICREFERENCE` | CHAR(20) |  |  |  |  |
| 73 | `NEWBOMPLANTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 74 | `NEWBOMPLANTCODE` | CHAR(8) |  |  |  |  |
| 75 | `NEWBOMCOSTGROUPCODE` | CHAR(3) |  |  |  |  |
| 76 | `NEWBOMSTCGROUPCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 77 | `NEWBOMSTATISTICALGROUPCODE` | CHAR(6) |  |  |  |  |
| 78 | `NEWBOMCOLLECTIONGRPCMYCODE` | CHAR(3) |  |  |  |  |
| 79 | `NEWBOMCOLLECTIONGROUPCODE` | CHAR(6) |  |  |  |  |
| 80 | `NEWBOMBOMUOMTYPE` | CHAR(2) |  |  |  |  |
| 81 | `NEWBOMBOMUOMCODE` | CHAR(3) |  |  |  |  |
| 82 | `NEWBOMBOMQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 83 | `NEWBOMBOMINCIDENCE` | DECIMAL(5,2) |  |  |  |  |
| 84 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 85 | `NEWBOMREMAPTOCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 86 | `COPYRULES` | SMALLINT | NOT NULL |  |  |  |
| 87 | `COPYQUICKRULES` | SMALLINT | NOT NULL |  |  |  |
| 88 | `COPYDIRECTIVES` | SMALLINT | NOT NULL |  |  |  |

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
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.PRODUCTITEMCODE,
       t.PRODUCTSUBCODE01,
       t.PRODUCTSUBCODE02,
       t.PRODUCTSUBCODE03,
       t.PRODUCTSUBCODE04,
       t.PRODUCTSUBCODE05
FROM   DB2ADMIN.WRKFATHERCHILDPRODUCT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
