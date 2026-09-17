# DB2ADMIN.WORKCENTERANDOPERATTRSBEAN

> **DO NOT QUERY FOR BUSINESS DATA.** Integration staging/import mirror. Holds in-flight inbound rows, not the authoritative record, and relaxes the NOT NULL constraints of its twin. Do NOT use for business reporting.

- **Module**: `PRODUCTION` (high confidence — table name starts with 'WORKCENTER')
- **Roles**: `staging_mirror`, `child_of_implicit_parent`
- **Columns**: 115
- **Primary key**: `IMPORTAUTOCOUNTER`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 75078

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FATHERID` | BIGINT | NOT NULL |  | implicit_parent_ref | Implicit parent-row pointer holding the parent table's ABSUNIQUEID. NOT declared as a foreign key anywhere -- the parent table is resolved by the application, not the schema. Join as: parent.ABSUNIQUEID = child.FATHERID. |
| 1 | `IMPORTAUTOCOUNTER` | BIGINT | NOT NULL | PK | primary_key staging | Staging-row sequence number. Its presence marks a *BEAN import/staging mirror table. |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 4 | `OPERATIONCODE` | CHAR(8) |  |  |  |  |
| 5 | `CODE` | CHAR(20) |  |  |  | Business (natural) key of a master-data table, typically the last primary-key column. |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `PRODRESERVATIONLINKGROUPCODE` | CHAR(20) |  |  |  |  |
| 10 | `STANDARDSTEPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 11 | `STANDARDSTEPQTYUOMCODE` | CHAR(3) |  |  |  |  |
| 12 | `STEPEFFICIENCYAPPLY` | CHAR(1) |  |  |  |  |
| 13 | `STEPEFFICIENCY` | DECIMAL(5,2) |  |  |  |  |
| 14 | `SESSIONSTEP` | CHAR(2) |  |  |  |  |
| 15 | `NROFMACHINEPOLICYCODE` | CHAR(20) |  |  |  |  |
| 16 | `REPETITIONNUMBER` | DECIMAL(17,6) |  |  |  |  |
| 17 | `BATHVOLUME` | DECIMAL(17,6) |  |  |  |  |
| 18 | `BATHVOLUMEUOMCODE` | CHAR(3) |  |  |  |  |
| 19 | `CURRENTSTEPPROGRESS` | CHAR(1) |  |  |  |  |
| 20 | `PREVIOUSSTEPPROGRESS` | CHAR(1) |  |  |  |  |
| 21 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 22 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 23 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 24 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 25 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 26 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 27 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 28 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 29 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 30 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 31 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 32 | `SUFFIXCODE` | CHAR(20) |  |  |  |  |
| 33 | `NUMBERID` | DECIMAL(11,0) |  |  |  |  |
| 34 | `OPSTEPGROUPCODE` | CHAR(8) |  |  |  |  |
| 35 | `LOSSINCREASETYPE1CODE` | CHAR(3) |  |  |  |  |
| 36 | `LOSSINCREASE1` | DECIMAL(15,5) |  |  |  |  |
| 37 | `LOSSINCREASEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 38 | `LOSSINCREASETYPE2CODE` | CHAR(3) |  |  |  |  |
| 39 | `LOSSINCREASE2` | DECIMAL(15,5) |  |  |  |  |
| 40 | `LOSSINCREASEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 41 | `LOSSINCREASETYPE3CODE` | CHAR(3) |  |  |  |  |
| 42 | `LOSSINCREASE3` | DECIMAL(15,5) |  |  |  |  |
| 43 | `LOSSINCREASEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 44 | `LOSSINCREASETYPE4CODE` | CHAR(3) |  |  |  |  |
| 45 | `LOSSINCREASE4` | DECIMAL(15,5) |  |  |  |  |
| 46 | `LOSSINCREASEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 47 | `LOSSINCREASETYPE5CODE` | CHAR(3) |  |  |  |  |
| 48 | `LOSSINCREASE5` | DECIMAL(15,5) |  |  |  |  |
| 49 | `LOSSINCREASEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 50 | `LOSSINCREASETYPE6CODE` | CHAR(3) |  |  |  |  |
| 51 | `LOSSINCREASE6` | DECIMAL(15,5) |  |  |  |  |
| 52 | `LOSSINCREASEREFUOM6CODE` | CHAR(3) |  |  |  |  |
| 53 | `LOSSINCREASETYPE7CODE` | CHAR(3) |  |  |  |  |
| 54 | `LOSSINCREASE7` | DECIMAL(15,5) |  |  |  |  |
| 55 | `LOSSINCREASEREFUOM7CODE` | CHAR(3) |  |  |  |  |
| 56 | `LOSSINCREASETYPE8CODE` | CHAR(3) |  |  |  |  |
| 57 | `LOSSINCREASE8` | DECIMAL(15,5) |  |  |  |  |
| 58 | `LOSSINCREASEREFUOM8CODE` | CHAR(3) |  |  |  |  |
| 59 | `PLANNINGLEADTIME` | DECIMAL(15,5) |  |  |  |  |
| 60 | `TIMETYPE1CODE` | CHAR(3) |  |  |  |  |
| 61 | `TIME1` | DECIMAL(10,5) |  |  |  |  |
| 62 | `TIMEUNIT1` | CHAR(2) |  |  |  |  |
| 63 | `TIMEREFQTY1` | DECIMAL(15,5) |  |  |  |  |
| 64 | `TIMEREFUOM1CODE` | CHAR(3) |  |  |  |  |
| 65 | `TIMETYPE2CODE` | CHAR(3) |  |  |  |  |
| 66 | `TIME2` | DECIMAL(10,5) |  |  |  |  |
| 67 | `TIMEUNIT2` | CHAR(2) |  |  |  |  |
| 68 | `TIMEREFQTY2` | DECIMAL(15,5) |  |  |  |  |
| 69 | `TIMEREFUOM2CODE` | CHAR(3) |  |  |  |  |
| 70 | `TIMETYPE3CODE` | CHAR(3) |  |  |  |  |
| 71 | `TIME3` | DECIMAL(10,5) |  |  |  |  |
| 72 | `TIMEUNIT3` | CHAR(2) |  |  |  |  |
| 73 | `TIMEREFQTY3` | DECIMAL(15,5) |  |  |  |  |
| 74 | `TIMEREFUOM3CODE` | CHAR(3) |  |  |  |  |
| 75 | `TIMETYPE4CODE` | CHAR(3) |  |  |  |  |
| 76 | `TIME4` | DECIMAL(10,5) |  |  |  |  |
| 77 | `TIMEUNIT4` | CHAR(2) |  |  |  |  |
| 78 | `TIMEREFQTY4` | DECIMAL(15,5) |  |  |  |  |
| 79 | `TIMEREFUOM4CODE` | CHAR(3) |  |  |  |  |
| 80 | `TIMETYPE5CODE` | CHAR(3) |  |  |  |  |
| 81 | `TIME5` | DECIMAL(10,5) |  |  |  |  |
| 82 | `TIMEUNIT5` | CHAR(2) |  |  |  |  |
| 83 | `TIMEREFQTY5` | DECIMAL(15,5) |  |  |  |  |
| 84 | `TIMEREFUOM5CODE` | CHAR(3) |  |  |  |  |
| 85 | `WORKCENTERTYPE` | CHAR(2) |  |  |  |  |
| 86 | `WSOPERATION` | INTEGER | NOT NULL |  | staging | Requested web-service operation for a staging row (integration inbox pattern). |
| 87 | `IMPORTSTATUS` | INTEGER | NOT NULL |  | staging | Staging-row processing status (integration inbox pattern). |
| 88 | `IMPCREATIONDATETIME` | TIMESTAMP |  |  |  |  |
| 89 | `IMPCREATIONUSER` | CHAR(50) |  |  |  |  |
| 90 | `IMPLASTUPDATEDATETIME` | TIMESTAMP |  |  |  |  |
| 91 | `IMPLASTUPDATEUSER` | CHAR(50) |  |  |  |  |
| 92 | `IMPORTDATETIME` | TIMESTAMP |  |  |  |  |
| 93 | `RETRYNR` | INTEGER | NOT NULL |  | staging | Retry attempt counter for a staging row. |
| 94 | `NEXTRETRY` | BIGINT | NOT NULL |  | staging | Next retry timestamp for a failed staging row. |
| 95 | `IMPORTID` | BIGINT | NOT NULL |  |  |  |
| 96 | `RELATEDDEPENDENTID` | BIGINT | NOT NULL |  |  |  |
| 97 | `TRANSLATEDLONGDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 98 | `TRANSLATEDLANGUAGECODE` | CHAR(2) |  |  |  |  |
| 99 | `TRANSLATEDSHORTDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 100 | `PARALLELPDNUMBER` | INTEGER | NOT NULL |  |  |  |
| 101 | `PICKUPQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 102 | `GENERATEAUTOMATICQATEST` | SMALLINT | NOT NULL |  |  |  |
| 103 | `IMPOPERATIONUSER` | CHAR(50) |  |  |  |  |
| 104 | `FORCEDWARNING` | SMALLINT | NOT NULL |  |  |  |
| 105 | `EXCLUDEFINITECAPACITY` | SMALLINT | NOT NULL |  |  |  |
| 106 | `EXCLUDECHECKOVERCAPACITY` | SMALLINT | NOT NULL |  |  |  |
| 107 | `PROTOTYPE` | SMALLINT | NOT NULL |  |  |  |
| 108 | `PROTOTYPEPROJECT` | CHAR(16) |  |  |  |  |
| 109 | `PROTOTYPEVERSION` | CHAR(3) |  |  |  |  |
| 110 | `OVERLAPPINGWITHPREVSTEPRULE` | INTEGER | NOT NULL |  |  |  |
| 111 | `OVERLAPPINGTONEXTSTEPRULE` | INTEGER | NOT NULL |  |  |  |
| 112 | `NUMBEROFHOURS` | DECIMAL(10,5) |  |  |  |  |
| 113 | `QUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 114 | `QUANTITYUOMCODE` | CHAR(3) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Implicit links (NOT declared in the DDL — inferred)

- `FATHERID` → **parent not derivable**. FATHERID present but no parent table is derivable from the name. Join as `WORKCENTERANDOPERATTRSBEAN.FATHERID = <parent>.ABSUNIQUEID`, where `<parent>` must come from the query context.

## Indexes

- `WORKCENTERANDOPERATTRSBEANXMT` (IMPORTSTATUS, RETRYNR, IMPORTAUTOCOUNTER, NEXTRETRY)

## Starter query

```sql
SELECT t.FATHERID,
       t.IMPORTAUTOCOUNTER,
       t.COMPANYCODE,
       t.WORKCENTERCODE,
       t.OPERATIONCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.PRODRESERVATIONLINKGROUPCODE,
       t.STANDARDSTEPQUANTITY,
       t.STANDARDSTEPQTYUOMCODE
FROM   DB2ADMIN.WORKCENTERANDOPERATTRSBEAN t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
