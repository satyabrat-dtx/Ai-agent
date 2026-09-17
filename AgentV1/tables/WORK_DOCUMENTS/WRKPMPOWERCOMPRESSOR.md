# DB2ADMIN.WRKPMPOWERCOMPRESSOR

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 49
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 94609

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `INSPECTIONDATE` | DATE |  |  |  |  |
| 4 | `PLANTCODE` | CHAR(3) |  |  |  |  |
| 5 | `PLANTDESC` | VARCHAR(200) |  |  |  |  |
| 6 | `DEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 7 | `DEPARTMENTDESC` | VARCHAR(200) |  |  |  |  |
| 8 | `WORKCENTERCODE` | CHAR(8) |  |  |  |  |
| 9 | `WORKCENTERDESC` | VARCHAR(200) |  |  |  |  |
| 10 | `PMMACHINECOUNTERCODE` | CHAR(8) |  |  |  |  |
| 11 | `PMMACHINECODE` | CHAR(15) |  |  |  |  |
| 12 | `MACHINEDESC` | VARCHAR(200) |  |  |  |  |
| 13 | `METERREADING` | CHAR(10) |  |  |  |  |
| 14 | `RUNNINGHOURS` | CHAR(10) |  |  |  |  |
| 15 | `STEAMPRODUCTION` | CHAR(10) |  |  |  |  |
| 16 | `POWERCONSUMPTION` | CHAR(10) |  |  |  |  |
| 17 | `COALBOILER` | CHAR(10) |  |  |  |  |
| 18 | `HSDBOILER` | CHAR(10) |  |  |  |  |
| 19 | `HUSKBOILER` | CHAR(10) |  |  |  |  |
| 20 | `HEATGENERATED` | CHAR(10) |  |  |  |  |
| 21 | `THERMICPOWERCONSUMPTION` | CHAR(10) |  |  |  |  |
| 22 | `COALTHERMIC` | CHAR(10) |  |  |  |  |
| 23 | `HSDTHERMIC` | CHAR(10) |  |  |  |  |
| 24 | `HUSKTHERMIC` | CHAR(10) |  |  |  |  |
| 25 | `DGGENERATION` | CHAR(10) |  |  |  |  |
| 26 | `DGRUNNINGHOURS` | CHAR(10) |  |  |  |  |
| 27 | `UNITSGENERATED` | CHAR(10) |  |  |  |  |
| 28 | `HFOCONSUMED` | CHAR(10) |  |  |  |  |
| 29 | `HSDCONSUMED` | CHAR(10) |  |  |  |  |
| 30 | `AIRMETERREADING1` | CHAR(10) |  |  |  |  |
| 31 | `AIRMETERREADING2` | CHAR(10) |  |  |  |  |
| 32 | `AIRMETERREADING3` | CHAR(10) |  |  |  |  |
| 33 | `PMREADINGCOMPRESSOR` | CHAR(10) |  |  |  |  |
| 34 | `COMPRESSORPOWERCONSUMPTION` | CHAR(10) |  |  |  |  |
| 35 | `LEADINGHOURS` | CHAR(10) |  |  |  |  |
| 36 | `RAWMETERREADING` | CHAR(10) |  |  |  |  |
| 37 | `RAWWATERGENERATED` | CHAR(10) |  |  |  |  |
| 38 | `RAWPOWERCONSUMPTION` | CHAR(10) |  |  |  |  |
| 39 | `BIOMETERREADING` | CHAR(10) |  |  |  |  |
| 40 | `BIOGASGENERATED` | CHAR(10) |  |  |  |  |
| 41 | `BIOPOWERCONSUMPTION` | CHAR(10) |  |  |  |  |
| 42 | `POWER` | CHAR(10) |  |  |  |  |
| 43 | `STEAM` | CHAR(10) |  |  |  |  |
| 44 | `PROPANE` | CHAR(10) |  |  |  |  |
| 45 | `SOFTWATER` | CHAR(10) |  |  |  |  |
| 46 | `THERMICHEAT` | CHAR(10) |  |  |  |  |
| 47 | `HALLUSERGROUPTYPE` | CHAR(3) |  |  |  |  |
| 48 | `HALLCODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.LINENO,
       t.INSPECTIONDATE,
       t.PLANTCODE,
       t.PLANTDESC,
       t.DEPARTMENTCODE,
       t.DEPARTMENTDESC,
       t.WORKCENTERCODE,
       t.WORKCENTERDESC,
       t.PMMACHINECOUNTERCODE,
       t.PMMACHINECODE
FROM   DB2ADMIN.WRKPMPOWERCOMPRESSOR t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
