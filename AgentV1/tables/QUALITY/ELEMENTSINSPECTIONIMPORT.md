# DB2ADMIN.ELEMENTSINSPECTIONIMPORT

- **Module**: `QUALITY` (low confidence — table name starts with 'ELEMENT')
- **Roles**: `business_data`
- **Columns**: 68
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `EVENTSLINK`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 8566

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 1 | `IMPORTCODE` | CHAR(15) |  |  |  |  |
| 2 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `ELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 5 | `ELEMENTCODE` | CHAR(15) |  |  |  |  |
| 6 | `EVENTSLINK` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 7 | `NUMBERGROUPSHIFT` | INTEGER | NOT NULL |  |  |  |
| 8 | `NUMBERSHIFT` | INTEGER | NOT NULL |  |  |  |
| 9 | `OPERATORCODE` | CHAR(50) |  |  |  |  |
| 10 | `WEAVERCODE` | CHAR(50) |  |  |  |  |
| 11 | `DEMANDCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 12 | `DEMANDCODE` | CHAR(15) |  |  |  |  |
| 13 | `DLVPURORDLINEPURORDCNTCODE` | CHAR(8) |  |  |  |  |
| 14 | `DLVPURORDLINEPURORDERCODE` | CHAR(15) |  |  |  |  |
| 15 | `DLVPURCHASEORDERLINEORDERLINE` | DECIMAL(7,0) |  |  |  |  |
| 16 | `DLVPURORDERLINEORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 17 | `DELIVERYDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |
| 18 | `PACKINGTYPECODE` | CHAR(3) |  |  |  |  |
| 19 | `LENGTHUOMCODE` | CHAR(3) |  |  |  |  |
| 20 | `LENGTHINITIAL` | DECIMAL(7,2) |  |  |  |  |
| 21 | `LENGTHGROSS` | DECIMAL(7,2) |  |  |  |  |
| 22 | `WEIGHTUOMCODE` | CHAR(3) |  |  |  |  |
| 23 | `WEIGHTGROSS` | DECIMAL(7,2) |  |  |  |  |
| 24 | `WEIGHTNET` | DECIMAL(7,2) |  |  |  |  |
| 25 | `WEIGHTREALNET` | DECIMAL(7,2) |  |  |  |  |
| 26 | `WIDTHUOMCODE` | CHAR(3) |  |  |  |  |
| 27 | `WIDTHGROSS` | DECIMAL(7,2) |  |  |  |  |
| 28 | `WIDTHNET` | DECIMAL(7,2) |  |  |  |  |
| 29 | `QUALITYCODE` | DECIMAL(2,0) |  |  |  |  |
| 30 | `QUALITYREASONCODE` | CHAR(3) |  |  |  |  |
| 31 | `TOTALPOINTS` | DECIMAL(5,0) |  |  |  |  |
| 32 | `TOTALCREDITS` | DECIMAL(7,2) |  |  |  |  |
| 33 | `NUMBEROFPIECES` | DECIMAL(5,0) |  |  |  |  |
| 34 | `NUMBEROFDEFECTS` | DECIMAL(5,0) |  |  |  |  |
| 35 | `NUMBEROFDEFECTSINCALC` | DECIMAL(5,2) |  |  |  |  |
| 36 | `SHORTESTPIECELENGHT` | DECIMAL(7,2) |  |  |  |  |
| 37 | `PREDOMINANTDEFECTEVENTCODE` | CHAR(3) |  |  |  |  |
| 38 | `PREDEFECTGRPSTDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 39 | `PREDOMINANTDEFECTGROUPCODE` | CHAR(3) |  |  |  |  |
| 40 | `QUALITYTABLESTDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 41 | `QUALITYTABLECODE` | CHAR(3) |  |  |  |  |
| 42 | `POINTTABLESTDGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 43 | `POINTTABLECODE` | CHAR(3) |  |  |  |  |
| 44 | `VARIABLE` | VARCHAR(250) |  |  |  |  |
| 45 | `INSPECTIONSTARTDATETIME` | TIMESTAMP |  |  |  |  |
| 46 | `INSPECTIONENDDATETIME` | TIMESTAMP |  |  |  |  |
| 47 | `INSPECTIONTIME` | TIME |  |  |  |  |
| 48 | `INSPECTIONSTOPTIME` | TIME |  |  |  |  |
| 49 | `LOOMNUMBER` | CHAR(10) |  |  |  |  |
| 50 | `INSPECTIONSTATION` | CHAR(10) |  |  |  |  |
| 51 | `WINDINGMACHINE` | CHAR(10) |  |  |  |  |
| 52 | `ORIGINALELEMENTITEMTYPECODE` | CHAR(3) |  |  |  |  |
| 53 | `ORIGINALELEMENTSUBCODEKEY` | CHAR(20) |  |  |  |  |
| 54 | `ORIGINALELEMENTCODE` | CHAR(15) |  |  |  |  |
| 55 | `ADUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 56 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 57 | `ELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 58 | `OPERATORCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 59 | `WEAVERCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 60 | `QUALITYITEMTYPECOMPANYCODE` | CHAR(3) |  |  |  |  |
| 61 | `QUALITYREASONCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 62 | `PREDEFECTGRPSTDGRPTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 63 | `QUALITYTABLESTDGRPTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 64 | `POINTTABLESTDGRPTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 65 | `ORIGINALELMITEMTYPECMYCODE` | CHAR(3) |  |  |  |  |
| 66 | `ORIGINALELEMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 67 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ELEMENTSINSIMP01` (IMPORTCODE)
- `ELEMENTSINSPECTIONIMPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.IMPORTSTATUS,
       t.IMPORTCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.ELEMENTSUBCODEKEY,
       t.ELEMENTCODE,
       t.EVENTSLINK,
       t.NUMBERGROUPSHIFT,
       t.NUMBERSHIFT,
       t.OPERATORCODE,
       t.WEAVERCODE,
       t.DEMANDCOUNTERCODE
FROM   DB2ADMIN.ELEMENTSINSPECTIONIMPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
